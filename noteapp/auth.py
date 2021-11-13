from flask import Blueprint, render_template, request, flash
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# app = Flask(__name__)
# app.config.from_object(Config)

# db = SQLAlchemy(app)
# migrate= Migrate(app, db)

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    #  "<p>Login After Registering</p>"
    
    data = request.form
    print(data)
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        firstName = request.form.get('firstname')
        password = request.form.get('password')
        
        #if its not valid include what to do
        if len(email) < 4:
            flash('Invalid, too short', category='error')
        elif len(password) < 3:
            flash('Invalid, too short', category='error')
        else: 
            flash('Awesome!', category='success')
    return render_template('sign_up.html')

@auth.route('/register')
def register():
    return "<p>Register to be able to login</p>"

@auth.route('/my_account')
def my_account():
    return "<p>My Account To see the </p>"

@auth.route('/my_notes')
def my_notes():
    return "<p>My Notes View posted or uploaded notes</p>"

@auth.route('/my_jobs')
def my_jobs():
    return "<p>My Jobs - Notetakers view PAST jobs, CURRENT Jobs, PENDING jobs</p>"