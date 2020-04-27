# import sys
# sys.path.append("/home/medvet/PycharmProjects/phrases/")
#
# from phrases.run import auth
#
#
# auth.User.create_table(fail_silently=True)
# admin = auth.User(username="admin", email="email@example.com", admin=True, active=True)
# admin.set_password("admin")
# admin.save()

# curl -u admin:admin -d data='{"volume': 1, "sentence": "hello api", "translation": "привет апи!"}' http://127.0.0.1:5000/api/phrase/