# README #
</h2>Root Files</h2>
* `__init__.py`: Instantiates the flask app and connects it to the database

* `.flaskenv`: registers environment variables that you want to be automatically imported when you run the `flask` command (requires the `python-dotenv` package). Critical to change FLASK_DEBUG to 0 when switching to production.

* `app.db`: our database

* `config.py`: configures the database (and maybe more stuff?)

* `database_visual.xml`: An XML file that can be imported to https://ondras.zarovi.cz/sql/demo/ to visualize the database (not the same - yet - as that in `app.db`) and will allow us to create the code for the database (if needed) as well.

* `db_models.py`: defines the database schema

* `requirements.txt`: will contain all package dependencies for the website (useful for Docker down the road)

* `yadayada.py`: the meat

<h2>Folders</h2>
* `migrations`: Created by flask_migrate.  Utilizes Alembic to facilitate changes to our database (e.g. if we add a new field).  Should be included in version control.

* `enums`: outlines description & functionality of user permissions
* `views`: to contain blueprints for pages

<h2>Reminders for Production</h2>
* Turn off Flask's debug mode
* Set the SECRET_KEY (in config.py) to something unique and difficult to guess
