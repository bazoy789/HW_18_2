from flask import Flask
from flask_restx import Api

from setup_db import db
from views.directors import directors_ns
from views.genre import genres_ns
from views.movie import movies_ns
from config import Config

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    configure(app)
    return app


def configure(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(directors_ns)

app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host='localhost', port=10001, debug=True)
