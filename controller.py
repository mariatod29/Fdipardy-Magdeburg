import tkinter as tk
import keyboard
import winsound
from model import Model
from view import View


class Controller(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.withdraw()  # hide default window
        self.view = View(self)
        self.player_scores = {1: 0, 2: 0, 3: 0}
        self.buzz_order = {}

        # define the buzzer sound frequency and duration
        self.BUZZER_FREQ = 440  # in Hz
        self.BUZZER_DURATION = 1000  # in milliseconds

        # define the buzzer keys for each player
        self.BUZZER_KEYS = {
            1: '1',
            2: '2',
            3: '3'
        }

        # set up the key listeners for each player's buzzer key
        for player, key in self.BUZZER_KEYS.items():
            keyboard.add_hotkey(key, self.handle_buzzer, args=(player,), suppress=True)

    def handle_buzzer(self, player):
        # check if this player has already buzzed in
        if player in self.buzz_order:
            return

        # add the player to the buzz order and play the buzzer sound
        self.buzz_order[player] = len(self.buzz_order) + 1
        self.play_buzzer()

        # add the score to the player's total score
        self.player_scores[player] += 1

        # disable all buttons
        self.view.disable_buttons()

        # check if all players have buzzed in
        if len(self.buzz_order) == len(self.BUZZER_KEYS):
            # show message box with the player who has the most points
            max_player = max(self.player_scores, key=self.player_scores.get)
            message = f"Player {max_player} has the most points!"
            self.view.show_message(message)

    def play_buzzer(self):
        winsound.Beep(self.BUZZER_FREQ, self.BUZZER_DURATION)

    def get_questions_and_answers(self, category, score, player_scores):
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
                'cc': answers[2]['correct'],
                'player_scores': self.player_scores
            }
            return questions_answers
        return {'question': 'No question found', 'answers': []}


if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(master=root)
    root.mainloop()
