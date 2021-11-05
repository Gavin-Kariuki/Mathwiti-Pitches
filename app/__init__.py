from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

#Initializing Flask Extensions
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations


    #configure UploadSet

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)