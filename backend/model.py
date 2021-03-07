import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'name': 'test01'
})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Facility(db.Model):
    __tablename__ = 'facility'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    type = db.Column(db.Integer)
    ward_id = db.Column(db.String(2))
    image_url = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, name, type, ward_id, image_url):
        self.name = name
        self.type = type
        self.ward_id = ward_id
        self.image_url = image_url
