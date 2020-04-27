from datetime import datetime

from peewee import *
from flask_peewee.admin import ModelAdmin
from flask_peewee.rest import RestResource

from phrases.app import db


class Volume(db.Model):

    name = CharField()


class Phrase(db.Model):

    volume = ForeignKeyField(Volume)
    sentence = CharField()
    translation = CharField()
    created = DateTimeField(default=datetime.now())


class NotePhrase(ModelAdmin):
    columns = ("sentence", "translation",)


class NoteVolume(ModelAdmin):
    columns = ("name",)


class UserResource(RestResource):
    exclude = ("password", "email",)
