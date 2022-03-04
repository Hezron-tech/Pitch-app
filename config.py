import os

class Config:


    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://hezron:hezzy@localhost/pitch'
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


 





