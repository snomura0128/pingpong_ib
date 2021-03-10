from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource

app = Flask(__name__, static_folder='../dist/static', template_folder='../dist')

app.config['SECRET_KEY'] = b'\xea\x8c\x9c\x18\x8eq_\xe2\x19\xab\x1b\t\x05\xa7\xfaF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'name': 'test01'
})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db = SQLAlchemy(app)


class Spam(Resource):
    def get(self):
        return [{
            "id": 1,
            "name": "新宿区コズミックセンター",
            "facilityTypes": [1],
            "imageUrl":
                "https://www.regasu-shinjuku.or.jp/regasu/wp-content/uploads/2010/04/3e37f68e2bd1b9c7d00bd1aa7e5f7844-420x296.jpg",
            "evaluation": 4.2,
            "favorite": True,
        }]


api.add_resource(Spam, '/api/search')


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
