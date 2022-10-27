
from crypt import methods
from flask_login import LoginManager,UserMixin
from flask_login import login_user, logout_user, current_user, login_required
from flask import Flask, render_template, request, flash,redirect,session,url_for

from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from model import Liked_Posts, Posts,app,db,Users,Friends,socketio
from forms import LoginForm, RegistrationForm,PostForm
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    return Users.query.filter_by(id=id).first()

def get_posts():
    posts = Posts.query.all()
    return [c.content for c in posts]

def add_posts(a_content):
    c = Posts(content= a_content,id = current_user.id)
    db.session.add(c)
    db.session.commit()
    
def like_a_post(post_id):
    like= Liked_Posts(posts_id=post_id)
    db.session.add(like)
    db.session.commit()
    
    
def get_friends(user_id):
    friends_list = Friends.query.filter_by(source_id=user_id).all()
    friends_list += Friends.query.filter_by(target_id=user_id).all()
    list_of_friends=[]
    for f in friends_list: 
        user_1 =  Users.query.filter_by(id=f.source_id).first()
        user_2 = Users.query.filter_by(id=f.target_id).first()
        if user_1.id == user_id:
           list_of_friends.append(user_2)    
        else: 
            list_of_friends.append(user_1)
   
    return list_of_friends

def add_friends(new_friend):
    
    f = Friends(source_id=current_user.id,target_id=new_friend)  
    db.session.add(f)
    db.session.commit()
      
@app.route("/")
@login_required
def index():

    posts = Posts.query.all()
    name = current_user.username
    
    return render_template("homepage.html",name=name,posts=posts)

@app.route("/get_friend", methods=['POST'])
def show_friends():
    get_friends(request.form['username'])
    return redirect(url_for('profile'))
@app.route("/add_friend",methods=["POST"])
def add_friend():
    
    add_friends(request.form['username']) 
    print(request.form['username'])
    return redirect (url_for('profile'))         
     
@app.route('/profile')
@login_required
def profile():
    friends = get_friends(current_user.id)
    users = Users.query.all()
    posts = Posts.query.all()
    name = current_user.username
    return render_template("profile.html",name=name,posts=posts,users=users,friends=friends)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password= generate_password_hash(form.password.data, method='sha256')
        username= form.username.data
        password=hashed_password
        
        new_register = Users(username=username, password=password)
        
        db.session.add(new_register)
        db.session.commit()
        
        flash("Registration complete! You may now login.")
        return redirect(url_for('login'))
    
    return render_template("registration.html", form=form) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == "POST":
        if form.validate_on_submit():
            user = Users.query.filter_by(username=form.username.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                
                    return redirect(url_for('index'))
                flash("Invalid")

    return render_template("login.html", form=form)


@app.route('/logout')
@login_required
def logout():
    """Log out."""
    logout_user()
    return redirect(url_for('login'))

@app.route('/posts', methods=['GET','POST'])
def posts():
    form=PostForm()
    
    if request.method == "POST":
        if form.validate_on_submit():
           content= form.content.data
           post = Posts(content,current_user.id)
           
           db.session.add(post)
           db.session.commit()
           
           return redirect(url_for('posts'))
    
    return render_template('posts.html', form=form)

@app.route('/like_post',methods=['POST'])
@login_required
def like_post():
    if like_a_post(request.form['content']):
        flash('Liked!')
    return redirect(url_for('index'))
@app.route('/session')
def sessions():
    return render_template('session.html')
    
def message_recieved(methods=['GET','POST']):
    print('message was recieved!')
    
@socketio.on('my event')
def message_board(json,methods=['GET','POST']):
    print('received my event'+ str(json))
    socketio.emit('my response',json, callback=message_recieved)
    
if __name__ == '__main__':
    app.run(debug=True)
    
if __name__=='__main__':
    socketio.run(app, debug=True)    
