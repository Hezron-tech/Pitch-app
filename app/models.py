from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model):

    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(1000))
    bio = db.Column(db.String(255))
    pitch = db.relationship("Pitch", backref="author", lazy="dynamic")
    profile_pic_path = db.Column(db.String())
    pass_secure  = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key=True)
    pitch_id = db.Column(db.Integer)
    pitch_title = db.Column(db.String)
    pitch_category = db.Column(db.String)
    pitch_itself = db.Column(db.String)
   
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    


    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_pitches(cls, category):
        pitches = Pitch.query.filter_by(pitch_category=category).all()
        return pitches
    @classmethod
    def getPitchId(cls, id):
        pitch = Pitch.query.filter_by(id=id).first()
        return pitch
    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


def __repr__(self):
        return f"Pitch ('{self.title}' , '{self.category}')"

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_itself = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment        









  





    

    

    


