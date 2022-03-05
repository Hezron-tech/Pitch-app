

from . import db



class User(db.Model):

    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(1000))
    bio = db.Column(db.String(255))
    pitch = db.relationship("Pitch", backref="author", lazy="dynamic")
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))

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





  





    

    

    


