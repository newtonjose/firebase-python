import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

dir = os.path.dirname(__file__)
KEY_PATH = os.path.join(dir,'serviceAccountKey.json')

cred = credentials.Certificate(KEY_PATH)
#firebase_admin.initialize_app(cred)

def quickstart_new_instance():
    # [START quickstart_new_instance]
    from google.cloud import firestore

    # Project ID is determined by the GCLOUD_PROJECT environment variable
    db = firestore.Client()
    # [END quickstart_new_instance]

    return db

try:
    #db = firestore.client()
    pass
except Exception as e:
    raise(e)
