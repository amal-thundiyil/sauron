import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sauron.backend.settings import DevelopmentSettings
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()


def create_app(config_class=DevelopmentSettings):
    app = Flask(__name__, static_folder="/static")
    app.config.from_object(config_class)
    db.init_app(app)
    bcrypt.init_app(app)
    if os.environ.get("FLASK_ENV") == "development":
        cors.init_app(app, resources=r"/*", origins="*", supports_credentials=True)

    from sauron.backend.server.api.auth import auth
    from sauron.backend.server.api.home import home
    from sauron.backend.server.api.dashboard import dashboard
    from sauron.backend.server.api.errors import errors

    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(errors)

    return app
