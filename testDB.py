from model import db

category = 'nahrung'
score = 20

doc_ref = db.collection(category).document(f"qu{score}")
doc = doc_ref.get()

if doc.exists:
    question_data = doc.to_dict()
    question_text = question_data.get('text')
    answers = [
        {
            'text': ans_data['text'],
            'correct': ans_data.get('correct', False) #set default to False if key not found
        }
        for ans_data in question_data.get('answers', {}).values()
    ]

    print(question_text)
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer['text']}")