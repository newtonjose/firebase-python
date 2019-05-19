import datetime
from helpers import db_new_instance
from models import City
import google.cloud.exceptions

def quickstart_add_data_one():
    db = db_new_instance()
    # [START quickstart_add_data_one]
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

def add_data_types():
    db = db_new_instance()
    # [START add_data_types]
    data = {
        u'stringExample': u'Hello, World!',
        u'booleanExample': True,
        u'numberExample': 3.14159265,
        u'dateExample': datetime.datetime.now(), 
        u'arrayExample': [5, True, u'hello'],
        u'nullExample': None,
        u'objectExample': {
            u'a': 5,
            u'b': True
        }
    }

    db.collection(u'data').document(u'one').set(data)
    # [END add_data_types]

def add_single_data():
    db = db_new_instance()
    
    doc_ref = db.collection(u'data').document(u'one')
    doc_ref.update({
            u'nullExample': 'NotNull'})

def add_cities():
    db = db_new_instance()
    
    cities_ref = db.collection(u'cities')
    
    cities_ref.document(u'LA').set(
        City(name='Los Angeles', state='CA', country='USA', capital=False, 
             population=3900000).to_struct())
    
    cities_ref.document(u'TOK').set(
        City(name='Tokyo', country='Japan', capital=True, 
             population=9000000).to_struct())
    
    cities_ref.document(u'DC').set(
        City(name='Washington D.C.', country='USA', capital=True, 
             population=680000).to_struct())
    
    cities_ref.document(u'SF').set(
            City(name="San Francisco", state="CA", country="USA", capital=False, 
                 population=860000).to_struct())

def add_city_with_generated_id():
    db = db_new_instance()
    
    c = City(name=u'Sao Paulo', state=u'SP', country=u'BRA', capital=False, 
                 population=11000000)
    
    db.collection(u'cities').add(c.to_struct())
    
    print(c.__repr__)
    
def get_check_exists():
    db = db_new_instance()
    # [START get_check_exists]
    doc_ref = db.collection(u'cities').document(u'SF')

    try:
        doc = doc_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
    except google.cloud.exceptions.NotFound:
        print(u'No such document!')
    # [END get_check_exists]
    
def get_full_collection():
    db = db_new_instance()
   
    docs = db.collection(u'cities').stream()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    
if __name__ == '__main__':
    ## Add a objet as data
    add_data_types()
    add_single_data()
    add_cities()
#    get_check_exists()
    get_full_collection()
#    add_city_with_generated_id()
    
    #r_fspython = GitRepo(name='Firestore-python', language='Python')
    #r_cs_2019 = GitRepo(name='CS-2019', language='JavaScript', stars=1)
    
    #u = GitUser(name='Josenilton', nickname='newtonjose')

    # Adicionar dados ao firestore
    #doc_ref = db.collection(u'gitusers').document(u.nickname)
    #doc_ref.set(u.)

    # Adicionar documentos filhos.    
    #repo_ref = doc_ref.collection(u'repos').document()
    #repo_ref.set(r_fspython.to_struct())
    
    #repo_ref = doc_ref.collection(u'repos').document()
    #repo_ref.set(r_cs_2019.to_struct())
    #print(u.to_struct())
    

