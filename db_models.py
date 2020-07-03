from app import db

"""
This file defines the database schema by inheriting the db.Model class from
SQLAlchemy in the creation of each table. Columns in each table inherit an
instance of the db.Column class.
"""
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(80), unique=False)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    transcription = db.Column(db.String(4000))
    filename = db.Column(db.String(120), nullable=False)
    privacy = db.Column(db.Boolean, default=True) #published vs. unpublished??? --AL

    def __repr__(self):
        return '<Video %r>' % self.title


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.STring(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    creation_date = db.Column(db.DateTime())
    password_hash = db.Column(db.String(30), unique=False) #store password hashes instead
    permission = db.Column(db.Integer, default=0, nullable=False) #maybe an ENUM type?
    email = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
