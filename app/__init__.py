from cgitb import strong
from ensurepip import bootstrap
from flask import Flask
import sqlalchemy
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import    SQLAlchemy
from flask_uploads import IMAGES, UploadSet, configure_uploads

db=SQLAlchemy()
mail=Mail()
bootstrap=Bootstrap()
login_manager=LoginManager()
login_manager.session_protection="strong"
login_manager.login_view="auth.login"
photos=UploadSet("photos",IMAGES)

def create_app(config_name)