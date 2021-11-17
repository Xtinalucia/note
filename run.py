from noteapp import app
from extensions import db


if __name__ == '__main__':
  
  from extensions import db
from flask_login import LoginManager
from noteapp.models import User
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is not None:
        return user
    else:
        return None
db.init_app(app)
with app.app_context():
     db.create_all()

app.run()
  
  
  

  
  # if __name__ == '__main__':
#     app.run() from line 4