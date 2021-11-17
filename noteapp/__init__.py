from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import *


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app = Flask(__name__)
# app.config['SECRECT_KEY']= 'Pythonsux'
    
from .notes import notes
from .auth import auth
    
app.register_blueprint(notes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
    

    