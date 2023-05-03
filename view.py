from tkinter import *
from tkinter import messagebox
from model import Model


class View:
    def __init__(self, controller):
        self.controller = controller
        self.root = Tk()
        self.root.title("Fdipardy")
        self.root.configure(background='white')
        self.root.geometry("1660x680")
        self.buttons = []
        self.labels = []

        # Initialize user scores and IDs
        self.player_scores = {"player1": 0, "player2": 0, "player3": 0}
        self.player_ids = ["player1", "player2", "player3"]
        self.current_player_index = 0
        self.player_score = 0
        self.player_scores = {}

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
        button.clicked = False  # add a clicked attribute to the button object
        command = lambda: self.on_click(button, category, score)
        button.config(command=command)
        if self.current_player_index == 0:
            button.config(state='normal')
        else:
            button.config(state='disabled')

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

        for button in self.buttons:
            if self.current_player_index == 0:
                button.config(state='normal')
            else:
                button.config(state='disabled')

    def on_click(self, button, category, score):
        if not button.clicked:
            # disabling the button after answering the question
            button.clicked = True
            button.config(state='disabled')
            question_window = Toplevel(self.root)
            question_window.geometry("1660x680")

            questions_answers = self.controller.get_questions_and_answers(category, score, player_scores=self.player_scores,
                                                                          player_id=self.player_ids[self.current_player_index])
            question = questions_answers["question"]
            answers = [questions_answers["a"], questions_answers["b"], questions_answers["c"]]

            correct_answer = None
            if questions_answers["ac"] == True:
                correct_answer = questions_answers["a"]
            elif questions_answers["bc"] == True:
                correct_answer = questions_answers["b"]
            elif questions_answers["cc"] == True:
                correct_answer = questions_answers["c"]

            question_score = questions_answers["score"]

            label = Label(question_window, text=question, width=90, height=3, font='Arial 20 bold', bd=4, bg='white')
            label.pack(side="top", pady=50, padx=20, anchor="center")
            self.labels.append(label)

            button_frame = Frame(question_window)
            button_frame.pack(side="top", pady=20)

            for i, ans in enumerate(answers):
                button = Button(button_frame, text=ans, width=40, height=2, font='Arial 15 bold', bd=4, fg='yellow',
                                bg='purple',
                                activeforeground='yellow', activebackground='white',
                                command=lambda selected_answer=ans, question_window=question_window: self.check_answer(selected_answer,
                                                                                               correct_answer,
                                                                                               question_score,
                                                                                               self.player_score, question_window))
                button.grid(row=0, column=i, padx=10)
                self.buttons.append(button)

    def check_answer(self, selected_answer, correct_answer, question_score, user_score, question_window):
        if selected_answer == correct_answer:
            self.player_score += question_score
            messagebox.showinfo("Correct answer", f"{self.player_ids[self.current_player_index]} answered correctly! "
                                                  f"They won {question_score} points! They now have {self.player_score}!")
        else:
            messagebox.showerror("Incorrect answer", "Incorrect! Better luck next time!")

        # Save the user score in the database
        model = Model()
        model.update_player_score(self.player_ids[self.current_player_index], self.player_score)

        # Move to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.player_ids)

        # Close the top-level window
        question_window.destroy()

