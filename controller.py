import tkinter as tk
from model import Model
from view import View

class Controller(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.withdraw()  # hide default window
        self.view = View(self)

    def get_questions_and_answers(self, category, score):
        doc_ref = Model.db.collection(f"{category}").document(f"qu{score}")
        doc = doc_ref.get()

        if doc.exists:
            question_data = doc.to_dict()
            question_text = question_data.get('text')
            question_score = question_data.get('score')

            answers = [
                {
                    'text': answer_data['text'],
                    'correct': answer_data.get('correct')
                }
                for answer_data in question_data.get('answers', {}).values()
            ]

            questions_answers = {
                'question': question_text,
                'a': answers[0]['text'],
                'b': answers[1]['text'],
                'c': answers[2]['text'],
                'score': question_score,
                'ac': answers[0]['correct'],
                'bc': answers[1]['correct'],
                'cc': answers[2]['correct']
            }
            return questions_answers
        return {'question': 'No question found', 'answers': []}

if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(master=root)
    root.mainloop()
