import os
from flask import Flask
from . import auth
from . import db
from .views import views_bp
from .views.item_views import item_views_bp
from . import profile


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Set the path to the instance folder within the dofus_web_app folder
    instance_path = os.path.join(app.root_path, 'instance')

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(instance_path, 'flaskr.sqlite'),
        CACHE_TYPE="SimpleCache",
        CACHE_DEFAULT_TIMEOUT=300
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Ensure the instance folder exists
    os.makedirs(instance_path, exist_ok=True)

    with app.app_context():
        db.init_app(app)
        app.register_blueprint(item_views_bp)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(views.views_bp)
        app.register_blueprint(profile.profile_bp)
        return app
