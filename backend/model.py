from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
postgresql_uri = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'name': 'test01'
})
app.config['SQLALCHEMY_DATABASE_URI'] = postgresql_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Facility(db.Model):
    __tablename__ = 'facilities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    ward_id = db.Column(db.String(2), nullable=False)
    image_url = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, name, type, ward_id, image_url):
        self.name = name
        self.type = type
        self.ward_id = ward_id
        self.image_url = image_url


class Ward(db.Model):
    __tablename__ = 'wards'

    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, name):
        self.name = name


class Favorites(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    facility_id = db.Column(db.Integer, nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, user_id, facility_id):
        self.user_id = user_id
        self.facility_id = facility_id
