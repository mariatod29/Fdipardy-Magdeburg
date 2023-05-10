from tkinter import *
from tkinter import messagebox
from model import Model
import tkinter as tk


class View:
    def __init__(self, controller):
        self.controller = controller
        self.player_ids = None
        self.player_scores = {}
        self.root = Tk()
        self.root.title("Fdipardy")
        self.root.configure(background='white')
        self.root.geometry("1660x720")
        self.buttons = []
        self.labels = []

        # Initialize user scores and IDs
        self.player_scores = {"player1": 0, "player2": 0, "player3": 0}
        self.player_ids = ["player1", "player2", "player3"]
        self.player_ids = [{"id": id, "score": 0} for id in self.player_ids]
        self.current_player_index = 0
        self.player_score = 0

        self.frame = Frame(self.root)
        self.frame.pack(fill="both", expand=True)

        self.scoreboard_frame = Frame(self.root)
        self.scoreboard_frame.pack(side="bottom", fill="x", padx=5, pady=5, anchor="center")

        # Add labels to display player scores
        for i, player_id in enumerate(self.player_ids):
            label = Label(self.scoreboard_frame, text=f"{player_id['id']}: {player_id['score']}", font="Arial 28 bold")
            label.grid(row=0, column=i, padx=175)
            self.labels.append(label)

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

    def disable_buttons(self):
        winner = self.controller.check_winner(self.player_scores)
        if winner is not None:
            winner_name = self.player_ids[winner]["id"]
            messagebox.showinfo("Winner", f"Congratulations {winner_name}! You won!")

        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def create_button(self, category, score):
        button = Button(self.frame, text=score + "$", width=20, height=2, font='Arial 25 bold', bd=4, fg="yellow",
                        bg="purple", activeforeground="yellow", activebackground="white")
        button.clicked = False  # add a clicked attribute to the button object
        command = lambda: self.on_click(button, category, score)
        button.config(command=command)
        if self.current_player_index == 0:
            button.config(state=NORMAL)
        else:
            button.config(state=DISABLED)

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

            questions_answers = self.controller.get_questions_and_answers(category, score,
                                                                          player_scores=self.player_scores,
                                                                          player_id=self.player_ids[
                                                                              self.current_player_index])
            question = questions_answers["question"]
            answers = [questions_answers["a"], questions_answers["b"], questions_answers["c"]]

            correct_answer = None
            if questions_answers["ac"]:
                correct_answer = questions_answers["a"]
            elif questions_answers["bc"]:
                correct_answer = questions_answers["b"]
            elif questions_answers["cc"]:
                correct_answer = questions_answers["c"]

            question_score = questions_answers["score"]

            label = Label(question_window, text=question, width=90, height=3, font='Arial 20 bold', bd=4, bg='white')
            label.pack(side="top", pady=50, padx=20, anchor="center")
            self.labels.append(label)

            button_frame = Frame(question_window)
            button_frame.pack(side="top", pady=20)

            player_score = self.player_score

            for i, ans in enumerate(answers):
                button = Button(button_frame, text=ans, width=40, height=2, font='Arial 16 bold', bd=4, bg='white',
                                command=lambda i=i: self.check_answer(question_window, answers[i], correct_answer,
                                                                      question_score, button_frame))
                button.pack(side="top", pady=10, padx=10, anchor="w")

    def check_answer(self, question_window, answer, correct_answer, question_score, button_frame):
        if answer == correct_answer:
            self.player_scores[self.player_ids[self.current_player_index]["id"]] += question_score
            self.labels[self.current_player_index].config(
                text=f"{self.player_ids[self.current_player_index]['id']}: {self.player_scores[self.player_ids[self.current_player_index]['id']]}")
            messagebox.showinfo("Correct!", f"Your answer '{answer}' is correct!")
        else:
            self.player_scores[self.player_ids[self.current_player_index]["id"]] -= question_score
            self.labels[self.current_player_index].config(
                text=f"{self.player_ids[self.current_player_index]['id']}: {self.player_scores[self.player_ids[self.current_player_index]['id']]}")
            messagebox.showerror("Wrong!",
                                 f"Your answer '{answer}' is incorrect! The correct answer is '{correct_answer}'.")

        question_window.destroy()

        # Update the current player index and score
        self.current_player_index = (self.current_player_index + 1) % len(self.player_ids)
        self.player_score = self.player_scores[self.player_ids[self.current_player_index]["id"]]

        # Disable buttons for other players and enable buttons for the current player
        for button in self.buttons:
            if self.current_player_index == 0:
                button.config(state='normal')
            else:
                button.config(state='disabled')

        # Check if the game is over and disable all buttons
        self.disable_buttons()