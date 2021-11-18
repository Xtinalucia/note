# from noteapp import db, login_manager
from sqlalchemy.sql.schema import ForeignKey
from extensions import db
import sqlalchemy as sa
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Lucid Chart: https://lucid.app/lucidchart/0fc2daf9-4561-4c02-9943-4d8ec666119d/edit?invitationId=inv_ac20fa1b-b93d-4fb0-8ab9-03b78de1b456&page=0_0#

class User(db.Model, UserMixin):
    # __tablename__ = 'User'
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    password = sa.Column(sa.String(128))
    course = sa.Column(sa.String(100))
    document_name = sa.Column(sa.String(100))
    Job_Id = sa.Column(sa.Integer, sa.ForeignKey('Jobs.Job_Id'))
    Jobs = sa.relationship('Jobs', backref='author', lazy=True)
   
    
    def __init__(self, username, email, user_id, document_name, Job_Id, password, course):
        self.id= user_id
        self.email = email
        self.username=username
        self.password = generate_password_hash(password)
        self.course = course
        self.document_name = document_name
        self.Job_Id = Job_Id
        
        
        
    # def check_password(self, password):
    #     return check_password_hash(self.password, password)
    
class NoteTaker(db.Model, UserMixin):
    # __tablename__ = 'NoteTaker'
    NoteTaker_id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    password = sa.Column(sa.String(128))
    course = sa.Column(sa.String(100))
    document_name = sa.Column(sa.String(100))
    Job_Id = sa.Column(sa.Integer, sa.ForeignKey('Jobs.Job_Id')) 
    
    def __init__(self, username, email, course, document_name, Job_Id, NoteTaker_id, password):
        self.NoteTaker_id = NoteTaker_id
        self.email = email
        self.username=username
        self.password = generate_password_hash(password)
        self.course = course
        self.document_name = document_name
        self.Job_Id = Job_Id
        
        
    # def check_password(self, password):
    #     return check_password_hash(self.password, password)
    
class School(db.Model, UserMixin):
    # __tablename__ = 'School'
    School_id = sa.Column(sa.Integer, primary_key=True)
    UofA_Arch100 = sa.Column(sa.String(50))
    UofB_Bio101 = sa.Column(sa.String(50))
    UofC_Chem101 = sa.Column(sa.String(50))
    
    def __init__(self, School_id, UofA_Arch100, UofB_Bio101, UofC_Chem101):
        self.School_id = School_id
        self.UofA_Arch100 = UofA_Arch100
        self.UofB_Bio101 = UofB_Bio101
        self.UofC_Chem101 = UofC_Chem101
   
class Jobs(db.Model, UserMixin):
    # __tablename__ = 'jobs'
    Job_Id = sa.Column(sa.Integer, primary_key=True)
    Pending_Jobs = sa.Column(sa.String(50))
    Current_Jobs = sa.Column(sa.String(50))
    Past_Jobs = sa.Column(sa.String(50))
    NoteTaker_id = sa.Column(sa.Integer, sa.ForeignKey('NoteTaker.NoteTaker_id'), nullable=False)
    id = sa.Column(sa.Integer, sa.ForeignKey('id'), nullable=False)
    date_created = sa.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    Date_Complete = sa.Column(sa.TIMESTAMP)
 # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __init__(self, Job_Id, Pending_Jobs, Current_Jobs, Past_Jobs, NoteTaker_id, id):
        self.Job_Id = Job_Id
        self.Pending_Jobs = Pending_Jobs
        self.Current_Jobs = Current_Jobs
        self.Past_Jobs = Past_Jobs
        self.NoteTaker_id = NoteTaker_id
        self.id = id
        
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

#sa.Column(sa.Integer, sa.ForeignKey('id'), nullable=False)