

from . import db



class User(db.Model):

    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(1000))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'



class Pitch(db.Model):

    __table__="pitch"

id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(255))
category =db.Column(db.String(255))
# users = db.relationship('User',backref = '',lazy="dynamic")





  





    

    

    


