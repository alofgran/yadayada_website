from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    transcription = db.Column(db.String(4000))
    filename = db.Column(db.String(120), nullable=False)
    privacy = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return '<Video %r>' % self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(30), unique=False)
    isadmin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def main():
    return render_template("test1.html", header="this is a test, my name is ryan")

@app.route("/<name>")
def name(name):
    return render_template("test1.html", header=name)

if __name__ == "__main__":
    app.run(debug=True)