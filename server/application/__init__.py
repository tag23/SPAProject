from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    db.init_app(app)
    csrf.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes

        db.create_all()
        return app
