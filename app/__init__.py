from flask import Flask
import sqlalchemy
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import    SQLAlchemy
# from flask_uploads import IMAGES, UploadSet, configure_uploads

db=SQLAlchemy()
from app.models import User,Pitch,Upvote,Downvote,Comment

mail=Mail()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection="strong"
login_manager.login_view="auth.login"
# photos=UploadSet("photos",IMAGES)

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    # configure_uploads(app,photos)

    mail = Mail()
 
    return app

    
