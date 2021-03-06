# from flask import session
# from sqlalchemy import ForeignKey, delete
from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255), unique=True, nullable=False)
    email=db.Column(db.String(255), unique=True, index = True, nullable=False)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    password_secure=db.Column(db.String(255), nullable=False)
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())

    pitches=db.relationship("Pitch",backref="user",lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    downvotes=db.relationship("Downvote",backref="user",lazy="dynamic")
    upvotes=db.relationship("Upvote",backref="user",lazy="dynamic")

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

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
        

class Pitch(db.Model):
    __tablename__="pitches"
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255), nullable=False)
    category=db.Column(db.String(255), index=True, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    time=db.Column(db.DateTime, default=datetime.utcnow)
    post=db.Column(db.Text(), nullable=False)
    downvotes=db.relationship("Downvote",backref="pitch",lazy="dynamic")
    upvotes=db.relationship("Upvote",backref="pitch",lazy="dynamic")
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
     
def save(self):
    db.session.add(self)
    db.session.commit()

def __repr__(self):
        return f"pitch:{self.post}" 

class Upvote(db.Model):
    __tablename__="upvotes"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer, db.ForeignKey('pitches.id'))

def save(self):
    db.session.add(self)
    db.session.commit()

def __repr__(self):
        return f"vote:{self.user_id}:{self.pitch_id}"

@classmethod
def display_upvotes(cls,id):
    upvote=Upvote.query.filter_by(pitch_id=id).all()

    return upvote

class Downvote(db.Model):
    __tablename__="downvotes"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer, db.ForeignKey('pitches.id'))

def save(self):
    db.session.add(self)
    db.session.commit()

def __repr__(self):
    return f"vote:{self.user_id}:{self.pitch_id}"

@classmethod
def display_upvotes(cls,id):
    downvote=Downvote.query.filter_by(pitch_id=id).all()

    return downvote

class Comment(db.Model):
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.Text(), nullable=False)

def save(self):
    db.session.add(self)
    db.session.commit()

@classmethod
def get_comments(cls,id):
    comments=Comment.query.filter_by(pitch_id=id).all()

    return comments

def __repr__(self):
    return f"comment{self.comment}"



