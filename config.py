import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','mysql://root:2811@localhost/axios')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY','Mango')