import firebase_admin
from firebase_admin import credentials, firestore

class Model:
    cred = credentials.Certificate('serviceAccount.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Specify the document ID and collection name
    doc_ref = db.collection('users').document('player1')

    def update_user_score(self, user_id, user_score):
        user_ref = self.db.collection('users').document(user_id)
        user_ref.update({'score': user_score})
