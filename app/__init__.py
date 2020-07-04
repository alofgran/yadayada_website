from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate #uses Alembic to enable changes to the database without needing to rebuild it
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, db_models #This must be placed at the end to avoid the circular imports problem
