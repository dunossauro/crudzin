from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serealizer import configure as config_ma


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MINHA CHAVE SECRETA'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crudzin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)

    from .user import bp_user
    app.register_blueprint(bp_user)

    return app
