from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES




# Instances of flask extensions
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
mail = Mail()
# Instance of LoginManger and using its methods
login_manager = LoginManager()

login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    '''
    Function that takes configuration setting key as an argument

    Args:
        config_name : name of the configuration to be used
    '''

    # Initialising application
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initialising flask extensions
    bootstrap.init_app(app)

    # Initializing database
    db.init_app(app)

    # Initializing login_manager
    login_manager.init_app(app)

    # Initializing mail
    mail.init_app(app)

    # Regestering the main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Regestering the auth bluprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # configure UploadSet
    configure_uploads(app,photos)


    # Setting config when using an API
    # from .requests import configure_request
    # configure_request(app)

    return app
