from tkinter import *
from firebaseConfig import db


def get_questions_and_answers(category, score):
    doc_ref = db.collection(f"{category}").document(f"qu{score}")
    doc = doc_ref.get()

    if doc.exists:
        question_data = doc.to_dict()
        question_text = question_data.get('text')
        answers = [
            {
                'text': answer_data['text'],
                'correct': answer_data.get('correct', False)  # set default to False if key not found
            }
            for answer_data in question_data.get('answers', {}).values()
        ]
        questions_answers = {
            'question': question_text,
            'a': answers[0]['text'],
            'b': answers[1]['text'],
            'c': answers[2]['text']
        }
        return questions_answers
    # Return a default value or raise an error if there is no valid question data
    return {'question': 'No question found', 'answers': []}


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Fdipardy")
        self.root.configure(background='white')
        self.root.geometry("1660x680")
        self.buttons = []  # define buttons attribute as empty list
        self.labels = []

        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.categories = ["Serien", "Nobelpreis", "Nahrung", "Schach"]

        for i, category in enumerate(self.categories):
            label = Label(self.frame, text=category, width=20, height=4, font="Arial 25 bold", bd=4, bg="white")
            label.grid(row=1, column=i, pady=25, sticky="ew")
            self.labels.append(label)

        btn_scores = [20, 40, 80, 100]

        self.row = 2
        self.column = 0

        for score in btn_scores:
            for category in self.categories:
                button = self.create_button(category.lower(), str(score))
                button.grid(row=self.row, column=self.column, pady=1, sticky="nsew")
                self.buttons.append(button)
                self.column += 1

                max_columns = 3

                if self.column > max_columns:
                    self.column = 0
                    self.row += 1

        # center the frame within the window
        self.frame.pack_configure(anchor="center")

    def create_button(self, category, score):
        button = Button(self.frame, text=score + "$", width=20, height=2, font='Arial 25 bold', bd=4, fg="yellow",
                        bg="purple", activeforeground="yellow", activebackground="white")
        command = lambda: self.on_click(category, score)
        button.config(command=command)
        return button

    def add_buttons(self):
        self.row = 2
        self.column = 0
        for category in self.categories:
            for score in [20, 40, 80, 100]:
                button = self.create_button(category, score)
                button.grid(row=self.row, column=self.column, pady=1, sticky="nsew")
                self.buttons.append(button)
                self.column += 1
                max_columns = 3
                if self.column > max_columns:
                    self.column = 0
                    self.row += 1

    def on_click(self, category, score):
        new = Toplevel(self.root)
        new.geometry("1660x680")

        questions_answers = get_questions_and_answers(category, score)
        question = questions_answers["question"]
        answers = [questions_answers["a"], questions_answers["b"], questions_answers["c"]]

        label = Label(new, text=question, width=90, height=3, font='Arial 20 bold', bd=4, bg='white')
        label.pack(side="top", pady=50, padx=20, anchor="center")
        self.labels.append(label)

        button_frame = Frame(new)
        button_frame.pack(side="top", pady=20)

        for i, ans in enumerate(answers):
            button = Button(button_frame, text=ans, width=40, height=2, font='Arial 15 bold', bd=4, fg='yellow',bg='purple',
                            activeforeground='yellow', activebackground='white')
            button.grid(row=0, column=i, padx=10)
            self.buttons.append(button)