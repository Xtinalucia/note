from flask import Blueprint, render_template, request, flash,  redirect, url_for
from flask import Flask, render_template, request
from sqlalchemy.exc import IntegrityError
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
import os

from .models import User, School, Jobs, Document, Link
from extensions import db
from sqlalchemy.exc import InterfaceError #do i need this one?



auth = Blueprint('auth','config', __name__)

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        school = request.form["school"]
        # document_name = request.form['document_name'] document_name=document_name,
        # user_id = request.form['user_id'] user_id=user_id,
        print(username, password)
        
        user = User.query.filter_by(school=school, username=username).first()
        # user = User.query.get(username)
        print(user)
        if user:
            if check_password_hash(user.password, password):
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
# How to Create
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        
        
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
            print("Email Already exists")
        print("User is Created")
    
    return render_template("register.html")

##################   to upload a file/s     ###################
#FROM DOCUMENTATION
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
            with open(filename, "r") as f:
                content = f.read()
                
            # Create document
            doc = Document(document_name=filename, text=content)  
            # Add current user as editor connecting thru db relationships
            doc.editors.append(User.query.get(current_user.id))
            
            # See if we got another editor add it
            editors = User.query.filter_by(username=request.form['editor']).all()
            if len(editors):
                doc.editors.append(editors[0])
           
            # Save changes
            db.session.add(doc)
            db.session.commit()
            
            return render_template('log.html',content=content,  mimetype='text/plain')
            
            # file.save(os.path.join('noteapp/static/upload', filename))  NOO!
            # file.save(os.path.join('http://127.0.0.1:5000/', filename))  NOO!
            # return redirect(url_for('auth.my_account', name=filename)) #go here after download  NOO!
        # code to check if name exisits NOO!
    # return '''NOO!
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''
    # return 'file uploaded successfully'
    
    return render_template('my_notes.html')
       
#Read uploaded document now in the db NOO!
@auth.route('/my_account')
def my_account():
    print("My Account To see the files after download complete")
    user = User.query.get(current_user.id)
    doc = user.documents[0] if len(user.documents) > 0 else False
    
    return render_template('my_account.html', documents=user.documents)
    return "<p>My Notes View posted or uploaded notes</p>"

@auth.route('/my_account/<int:id>', methods=['GET','POST'])
def view_note(id):
    if request.method == "POST":
        return redirect("auth/my_account")
    
    doc = Document.query.get(id)
    
    return render_template("note.html", note=doc)
           
           
           
# How to Delete ------------ from PhonebookApp ----Here deletion of document
@auth.route('/delete')
def delete():
    print("delete files after download complete")
    user = User.query.get(current_user.id)
    doc = user.documents[0] if len(user.documents) > 0 else False
    
    return render_template('delete.html', documents=user.documents)
    return "<p>My Notes View posted or uploaded notes</p>"

@auth.route('/delete/<int:id>',methods=['GET','POST'])
def delete_doc(id):
    doc = Document.query.get(id)#find the entry by id
    print(doc)
    print("How did i get here? Auth.py line 162")
    if not doc is None:#if found
        db.session.delete(doc)#delete entire entry
        db.session.commit()#commit
        
    return redirect("/auth/my_account")#refresh the page/#go bk to home page


# How to Update ----- phonebook + codemy
# @auth.route('/update')
# def update():
#     print("delete files after download complete")
#     user = User.query.get(current_user.id)
    
#     return render_template('update.html')
###########   How to Update  ################combo phonebook,register,delete,youtube codemy(JohnElder)
@auth.route('/update/', methods=['GET', 'POST'])
# @login_required
def update_info():
    
    user = User.query.get(current_user.id)#grab data
    name_to_update = User.query.get(current_user.id)
    if request.method == "POST":
        # user = User.query.get(current_user.id) duplicate
        print(user)
        print("Update files here!! Auth.py Line183! !")
    # name_to_update = User.query.get(id) WRONG!!!This does not match the user print statement from line 182!!!!
        name_to_update = User.query.get(current_user.id)
        print(name_to_update)
    
        
       # email = request.form['email'] NO!!!!
      #  username = request.form['username']  NO!!!!
        password = request.form['password']
        school = request.form['school']
        
       # name_to_update.email = email   NO!!!!
       # name_to_update.username = username   NO!!!!
        name_to_update.password = password
        name_to_update.school = school
        print("Working!!!!! Auth.py Line191! !")
        
        db.session.add(name_to_update)#dend data to db
        db.session.commit()
        flash("Updates made")
        print("hello")#where 2 view
        return render_template("update.html", name_to_update = name_to_update, id=current_user.id)
        
        # except:
        #     flash("This didnt work")
        #     return render_template("update.html", name_to_update = name_to_update, id=id)
    else:
        print("my name")
        return render_template("update.html", name_to_update = name_to_update, id = current_user.id)
  
# @auth.route('/upload')
# def upload_file():
#    return render_template('upload.html')

# @auth.route('/uploader', methods = ['GET', 'POST']) #this is doing the saving of the file
# def upload_file():
#    if request.method == 'POST':
#       f = request.files['file']
#       f.save(secure_filename(f.filename))
#       return 'ed successfully'



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