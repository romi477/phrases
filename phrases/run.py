from flask_peewee.auth import Auth
from flask_peewee.admin import Admin
from flask_peewee.rest import RestAPI, UserAuthentication

from phrases.app import app, db
from phrases.models import Phrase, Volume, NotePhrase, NoteVolume, UserResource


auth = Auth(app, db)
admin = Admin(app, auth)
user_auth = UserAuthentication(auth)
api = RestAPI(app, default_auth=user_auth)

if __name__ == "__main__":
    admin.register(Phrase, NotePhrase)
    admin.register(Volume, NoteVolume)
    auth.register_admin(admin)
    admin.setup()

    Phrase.create_table(fail_silently=True)
    Volume.create_table(fail_silently=True)
    auth.User.create_table(fail_silently=True)

    api.register(Phrase, UserResource)
    api.setup()

    app.run()
