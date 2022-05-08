import email
import profile

from sqlalchemy import delete
from . import db, login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__="users"
    id=db.Column(db.Integer, Primary_Key=True)
    username=db.Column(db.String(255), Unique=True, nullable=False)
    email=db.Column(db.String(255), Unique=True, nullable=False)
    secure_password=db.Column(db.String(255), nullable=False)
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    pitches=db.relationship("pitch",backref="user",lazy="dynamic")
    downvotes=db.relationship("downvote",backref="user",lazy="dynamic")
    upvotes=db.relationship("upvote",backref="user",lazy="dynamic")

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @property
    def set_password(self):
        raise AttributeError("You cannot read the password attribute")

    @set_password.setter
    def password(self,password):
        self.secure_password=generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)
    
    def save_u(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"user:{self.username}"
        

class Pitch(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, Primary_Key=True)
    username=db.Column(db.String(255), Unique=True, nullable=False)
    email=db.Column(db.String(255), Unique=True, nullable=False)
    secure_password=db.Column(db.String(255), nullable=False)
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    pitches=db.relationship("pitch",backref="user",lazy="dynamic")
    downvotes=db.relationship("downvote",backref="user",lazy="dynamic")
    upvotes=db.relationship("upvote",backref="user",lazy="dynamic")


