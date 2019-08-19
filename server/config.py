from os import environ, urandom


class Config:
    SECRET_KEY = "1337SecretKey"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/PostgreDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    FLASK_APP = environ.get('FLASK_APP')
    WTF_CSRF_ENABLED = False
