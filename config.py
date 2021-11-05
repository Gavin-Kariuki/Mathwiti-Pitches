import os

from instance.config import SECRET_KEY

class Config:
    '''General configuration class'''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY = os.environ.get('SECRET KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos' #we will store our photos in the static file since it is not advisable to that in the db

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig

}




