import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://postgres:123@localhost/translatica')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
