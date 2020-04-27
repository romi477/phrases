from flask import Flask
from flask_peewee.db import Database

from phrases.config import *


app = Flask(__name__)
app.config.from_object(Config)
db = Database(app)

from phrases import views
