import os
class Config:
    SECRET_KEY = 'ead4ba544d5d4f75942062f71d3b4720';
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    
    #mail configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    DEBUG = True


    
class ProdConfig(Config):
    
 SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

  


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
}