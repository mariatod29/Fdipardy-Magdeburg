from firebaseConfig import db

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

    # Get user input
    user_answer = input("Enter the number of the correct answer: ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(answers):
        selected_answer = answers[int(user_answer) - 1]
        if selected_answer['correct']:
            print("Congratulations! Your answer is correct.")
        else:
            print("Sorry, your answer is incorrect.")
    else:
        print(f"Invalid input. Please enter a number between 1 and {len(answers)}")
else:
    print(f"No document found with score {score}")