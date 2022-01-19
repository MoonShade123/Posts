from flask import Flask
from flask_alembic import Alembic

from posts.models import db
from posts.apis import api_v1


def create_app():
    app = Flask(__name__)
    app.config.from_object('posts.config.settings')

    db.init_app(app)
    api_v1.init_app(app)
    Alembic(app)

    return app
