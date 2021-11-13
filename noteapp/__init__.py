from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app = Flask(__name__)
# app.config['SECRECT_KEY']= 'Pythonsux'
    
from .views import views
from .auth import auth
    
app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
    

    