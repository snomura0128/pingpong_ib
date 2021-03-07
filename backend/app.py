from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xea\x8c\x9c\x18\x8eq_\xe2\x19\xab\x1b\t\x05\xa7\xfaF'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'admin',
    'password': 'admin',
    'host': '127.0.0.1',
    'name': 'test01'
})
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/hello')
def hello():
    return '<h1>こんにちわ</h1>'


@app.route('/')
def index():
    return render_template('index.html')


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
