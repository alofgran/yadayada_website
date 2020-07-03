from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #uses Alembic to enable changes to the database without needing to rebuild it
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes #This must be placed at the end to avoid the circular imports problem
