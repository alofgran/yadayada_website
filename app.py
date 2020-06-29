from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(100), unique=True)

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