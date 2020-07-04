from app import app, db
from app.db_models import Video, User, Professional, Admin

#This enables us to avoid importing our classes when running a python shell
#Now we can just run `flask shell` and begin working with the database
@app.shell_context_processor
def make_shell_context():
    return {
            'db': db,
            'Video': Video,
            'User': User,
            'Professional': Professional,
            'Admin': Admin
            }
