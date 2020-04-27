import os


class Config:
    DEBUG = True
    DATABASE = {
        "name": "phrases.sqlite",
        "engine": "peewee.SqliteDatabase",
    }
    SECRET_KEY = os.environ.get("SECRET_KEY")
