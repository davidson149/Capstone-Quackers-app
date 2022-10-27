const friend_container = document.getElementById('friend_container')

function toggle () {
    if (friend_container.style.visibility === 'visible') {
        friend_container.style.visibility = 'hidden';
    } else {
        friend_container.style.visibility = 'visible';
        
    }
}
document.getElementById('toggle-button').addEventListener('click', function () {
    toggle();
});
