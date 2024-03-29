import firebase_admin
from firebase_admin import credentials, firestore


class Model:
    cred = credentials.Certificate('serviceAccount.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    def update_player_score(self, player_id, player_score):
        player_ref = self.db.collection('users').document(player_id)
        player_ref.update({'score': player_score})
