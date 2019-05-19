import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dir = os.path.dirname(__file__)
KEY_PATH = os.path.join(dir,'serviceAccountKey.json')

cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)


try:
    db = firestore.client()
except Exception as e:
    raise(e)
