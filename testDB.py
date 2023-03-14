from firebaseConfig import db

nahrung_ref = db.collection(u'nahrung')
docs = nahrung_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
