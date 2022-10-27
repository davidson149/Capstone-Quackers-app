import os
from flask_socketio import SocketIO
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
app.secret_key="ABC"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
db= SQLAlchemy(app)
socketio= SocketIO(app)

class Users(db.Model, UserMixin):
    
    __tablename__="users"
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(250))
    posts = db.relationship('Posts',backref='user', lazy=True)
    
    def __init__(self, username, password):
       self.username = username
       self.password = password
    
    
class Posts(db.Model):
    
    __tablename__="posts"
    
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(Users.id))
    content = db.Column(db.Text(255))
    like = db.relationship('Liked_Posts',backref='post',lazy=True)
    
    def __init__(self, content,user_id):
        self.content = content
        self.user_id = user_id
class Liked_Posts(db.Model):
    
    __tablename__= "liked_posts"
    
    id = db.Column(db.Integer,primary_key=True)
    posts_id = db.Column(db.Integer,db.ForeignKey(Posts.id))
    
    def __repr__(self) -> str:
        return super().__repr__()
    
class Friends(db.Model):
    
    __tablename__ = "friends"
    
    id = db.Column(db.Integer,primary_key=True)
    source_id= db.Column(db.Integer, db.ForeignKey(Users.id))
    target_id= db.Column(db.Integer,db.ForeignKey(Users.id))
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    def get_users(self):
        friend_1=Users.query.get(self.source_id)
        friend_2=Users.query.get(self.target_id)
        return friend_1,friend_2
    
class Messages(db.Model):
    
    __tablename__="messages"
    
    id = db.Column(db.Integer,primary_key=True)
    source_id= db.Column(db.Integer, db.ForeignKey(Users.id))
    target_id= db.Column(db.Integer,db.ForeignKey(Users.id))
    content = db.Column(db.Text(255))
    
    def __repr__(self) -> str:
        return super().__repr__()
    

    
    
db.create_all()