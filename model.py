import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


class Model:
    def get_questions_and_answers(category, score):
        doc_ref = db.collection(f"{category}").document(f"qu{score}")
        doc = doc_ref.get()

        if doc.exists:
            question_data = doc.to_dict()
            question_text = question_data.get('text')
            answers = [
                {
                    'text': answer_data['text'],
                    'correct': answer_data.get('correct', False)
                }
                for answer_data in question_data.get('answers', {}).values()
            ]

            # Ensure that the dictionary contains keys 'a', 'b', and 'c' with default values if not present
            questions_answers = {
                'question': question_text,
                'a': answers[0]['text'] if len(answers) > 0 else '',
                'b': answers[1]['text'] if len(answers) > 1 else '',
                'c': answers[2]['text'] if len(answers) > 2 else ''
            }
            return questions_answers

        return {'question': 'No question found', 'a': '', 'b': '', 'c': ''}