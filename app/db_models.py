from datetime import datetime
from app import db

from werkzeug.security import generate_password_hash, check_password_hash
#Need to reduce repetition in password setting/checking

"""
This file defines the database schema by inheriting the db.Model class from
SQLAlchemy in the creation of each table. Columns in each table inherit an
instance of the db.Column class.
"""

#General users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(30), unique=False) #store password hashes instead
    creation_date = db.Column(db.DateTime(), default=datetime.utcnow)
    permission = db.Column(db.Integer, default=0, nullable=False) #maybe an ENUM type?

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


#Add in business information too (e.g. address, phone, etc.)?
class Professional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(14), nullable=True, unique=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(30), unique=False) #store password hashes instead
    creation_date = db.Column(db.DateTime())
    permission = db.Column(db.Integer, default=0, nullable=False) #maybe an ENUM type?
    posts = db.relationship('Video', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Professional %r>' % self.username


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    password_hash = db.Column(db.String(30), unique=False) #store password hashes instead
    permission = db.Column(db.Integer, default=0, nullable=False) #maybe an ENUM type?

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Admin %r>' % self.username

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('professional.id')) #class must be lowercase here
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    transcription = db.Column(db.String(4000))
    filename = db.Column(db.String(120), nullable=False)
    privacy = db.Column(db.Boolean, default=True) #published vs. unpublished??? --AL
    created_on = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('professional.id')) #value initializes as id field in professional class

    def __repr__(self):
        return '<Video %r>' % self.title
