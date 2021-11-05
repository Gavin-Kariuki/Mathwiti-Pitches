from enum import unique
from operator import index
from . import db
from flask_login import UserMixin, current_user
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime, time

class User(UserMixin,db.Model):

    '''class user with its properties'''

    __tablename__ = 'users'

    #nullable = False tells SQLAlchemy to create the column as NOT NULL

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(32),unique=True,nullable = False)
    email = db.Column(db.String(50),unique=True,nullable = False)
    pass_secure = db.Column(db.String(32),nullable = False)
    profile_pic_path = db.Column(db.String(50))

    

    def __repr__(self):
        return f'User {self.username}'

    @property
    def password(self):
        raise AttributeError('You can not access the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Pitch(db.Model):
    '''class pitch and its properties'''

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch = db.Column(db.Text(), nullable = False)
    time_posted = db.Column(db.DateTime, default = datetime.utcnow)
    category_of_the_pitch = db.Column(db.String(150), index = True, nullable = False)



    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.pitch}'

class Comment(db.Model):
    '''class comment and its properties'''

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key = True)
    



    

