from flask import Blueprint, render_template, request, flash,  redirect, url_for
from flask import Flask, render_template, request
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from flask_login import login_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import os



auth = Blueprint('auth','config', __name__)

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == "POST":
        from .models import User, School, Jobs
        username = request.form["username"]
        password = request.form["password"]
        school = request.form['school']
        # document_name = request.form['document_name'] document_name=document_name,
        # user_id = request.form['user_id'] user_id=user_id,
        print(username, password)
        
        user = User.query.filter_by(school=school, username=username, password=password).first()
    
    
        if user:
            login_user(user)
            print("User Logged in")
            return redirect(url_for("notes.home"))
        else:
            print("Something went wrong")
    
    return render_template('login.html', boolean=True)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        from .models import User, School, Jobs
        from extensions import db
        from sqlalchemy.exc import InterfaceError #do i need this one?
        
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        school = request.form['school']
        # document_name = request.form['document_name'] document_name=document_name,
        # user_id = request.form['user_id'] user_id=user_id,
        print(username, password, school, email)
        print('got to line 55')
        try:
        
            user = User(email=email, password=password, username=username, school=school)
            db.session.add(user)
            db.session.commit()
        except IntegrityError as e:
            print(e)
            print("Email Already exist")
        print("User is Created")
    
    return render_template("register.html")

##################   to upload a file/s     ###################
#
#https://flask.palletsprojects.com/en/2.0.x/patterns/fileuploads/ -----Uploading
@auth.route('/my_notes', methods=['GET','POST'])
def my_notes():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            f = request.files['file']
            f.save(secure_filename(f.filename))
            file.save(os.path.join('noteapp/static/upload', filename))
            # file.save(os.path.join('http://127.0.0.1:5000/', filename))
            return redirect(url_for('auth.my_account', name=filename)) #go here after download
        # code to check if name exisits
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
    return 'file uploaded successfully'
    
    return render_template('my_notes.html')
       
     
 
@auth.route('/my_account')
def my_account():
    print("My Account To see the files after download complete")
    return "<p>My Notes View posted or uploaded notes</p>"
       




# @auth.route('/upload')
# def upload_file():
#    return render_template('upload.html')

# @auth.route('/uploader', methods = ['GET', 'POST']) #this is doing the saving of the file
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'file uploaded successfully'



# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == "POST":
#         email = request.form.get('email')
#         firstName = request.form.get('firstname')
#         password = request.form.get('password')
        
#         #if its not valid include what to do
#         if len(email) < 4:
#             flash('Invalid, too short', category='error')
#         elif len(password) < 3:
#             flash('Invalid, too short', category='error')
#         else: 
#             flash('Awesome!', category='success')
#     return render_template('sign_up.html')
#@auth.route('/my_notes')
# def my_notes():
#     return "<p>My Notes View posted or uploaded notes</p>"