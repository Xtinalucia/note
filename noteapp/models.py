# from noteapp import db, login_manager
from sqlalchemy.sql.schema import ForeignKey
from extensions import db
import sqlalchemy as sa
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Lucid Chart: https://lucid.app/lucidchart/0fc2daf9-4561-4c02-9943-4d8ec666119d/edit?invitationId=inv_ac20fa1b-b93d-4fb0-8ab9-03b78de1b456&page=0_0#

class School(db.Model, UserMixin):
    # __tablename__ = 'School'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(50))
        
    def __init__(self, School_id, name):
        self.id = School_id
        self.name = name

class User(db.Model, UserMixin):
    # __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    password = sa.Column(sa.String(128))
    school = sa.Column(sa.Integer, sa.ForeignKey('school.id'))
    document_name = sa.Column(sa.String(100))
    documents = relationship('Document', secondary="link", back_populates="editors")
    
    
    def __init__(self, username, email, password, school):
        # self.id= user_id  user_id,
        self.email = email
        self.username=username
        self.password = generate_password_hash(password)
        self.school = school
        # self.document_name = document_name document_name,
        
        
   
class Jobs(db.Model, UserMixin):
    # __tablename__ = 'jobs'
    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.String(50))
    
    note_taker = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    hirer = sa.Column(sa.Integer, sa.ForeignKey('user.id'), nullable=False)
    date_created = sa.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_complete = sa.Column(sa.TIMESTAMP)
    
class Document(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True)
    document_name = sa.Column(sa.String(100))
    text = sa.Column(sa.String(10000))
    editors = relationship('User', secondary="link", back_populates="documents")
    

class Link(db.Model, UserMixin): #tie everything together and use relationships
    document_id = sa.Column(sa.Integer, sa.ForeignKey("document.id"), primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), primary_key=True)
       
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

#sa.Column(sa.Integer, sa.ForeignKey('id'), nullable=False)