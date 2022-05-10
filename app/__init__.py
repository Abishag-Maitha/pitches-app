from flask import Flask
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import    SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads


mail=Mail()
login_manager=LoginManager()
login_manager.session_protection="strong"
login_manager.login_view="auth.login"
photos=UploadSet("photos",IMAGES)

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    
    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initialzining flask packages
    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    
    #Registering Blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    configure_uploads(app,photos)
     
    return app

    
