import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('/Projects/Personal/firebase/tanklytics-firebase-adminsdk-fzpw5-fcfc0c8080.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


doc_ref = db.collection('userInfo').stream()

for doc in doc_ref:
    doc_dict = doc.to_dict()
    print(f'{doc.id} => {doc_dict}')

    name = doc_dict['name']
    print(name, '\n\n\n\n', doc_dict['facilityName'])


#doc = doc_ref.get()
#dict = doc.to_dict()

#print(dict)
