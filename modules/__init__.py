import toml
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import logging
import logging.config
import logging.handlers
import sys

db=SQLAlchemy()

def create_app(config_file):
    app=Flask(__name__,template_folder='../pages',static_folder='../resources')
    app.config.from_file(config_file,toml.load)

    db.init_app(app) 
    
    with app.app_context():
        from modules.login import login_bp 

        app.register_blueprint(login_bp,url_prefix='/sms')
    
    return app