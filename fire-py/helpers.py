import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dir = os.path.dirname(__file__)
KEY_PATH = os.path.join(dir,'config/serviceAccountKey.json')

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)


def db_new_instance():
    db = firestore.client()
    return db
