from flask_migrate import Migrate
from model import app, db


Migrate(app, db)
