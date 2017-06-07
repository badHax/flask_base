"""
basic controller for user authentication 
"""

from app_name import app
from app_name.models.user import User
from flask import Blueprint
from flask import Flask, Response, redirect, url_for, request, session, abort
from passlib.hash import pbkdf2_sha256
from flask.ext.login import LoginManager, UserMixin,\
                                login_required, login_user, logout_user 

#define  blueprint                               
authentication = Blueprint('authentication', __name__)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@authentication.route('/')
def index():
    return "Some Template"


# some protected url
@authentication.route('/')
@login_required
def home():
    return Response("Hello World!")

 
# somewhere to login
@authentication.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query(username=username).first()
        
        if user:
            if pbkdf2_sha256.verify(password+app.secret_key,user.password):
                login_user(user)
                return redirect(request.args.get("next"))
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


# somewhere to logout
@authentication.route("/logout")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


# handle login failed
@authentication.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')
    
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return User.query(userid=userid).first()