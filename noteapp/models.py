# from noteapp import db, login_manager
from extensions import db
import sqlalchemy as sa
# from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    username = sa.Column(sa.String(50), unique=True, nullable=False)
    password = sa.Column(sa.String(128))

    # def __init__(self, username, email, password):
    #     self.username=username
    #     self.email = email
    #     self.password = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)