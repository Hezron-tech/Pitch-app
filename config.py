import os

class Config:


    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = 'hezzy'
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/pitch'
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/pitch'


    DEBUG = True



     
config_options = {
'development':DevConfig,
'production':ProdConfig


}


   


 





