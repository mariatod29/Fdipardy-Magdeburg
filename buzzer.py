import keyboard
import winsound

# define the buzzer sound frequency and duration
BUZZER_FREQ = 440  # in Hz
BUZZER_DURATION = 1000  # in milliseconds

# define the buzzer keys for each player
BUZZER_KEYS = {
    1: '1',
    2: '2',
    3: '3'
}

# dictionary to keep track of which player buzzed in first
buzz_order = {}


# function to play the buzzer sound
def play_buzzer():
    winsound.Beep(BUZZER_FREQ, BUZZER_DURATION)


# function to handle a player buzzing in
def handle_buzzer(player):
    # check if this player has already buzzed in
    if player in buzz_order:
        return

    # add the player to the buzz order and play the buzzer sound
    buzz_order[player] = len(buzz_order) + 1
    play_buzzer()


# function to start the buzzer listening loop
def start_buzzer():
    # set up the key listeners for each player's buzzer key
    for player, key in BUZZER_KEYS.items():
        keyboard.add_hotkey(key, handle_buzzer, args=(player,), suppress=True)

    # start the keyboard listener loop
    keyboard.wait()

    # remove the key listeners when the loop is done
    for player, key in BUZZER_KEYS.items():
        keyboard.remove_hotkey(key)


# example usage
# start_buzzer()
# print(buzz_order)  # prints the order in which players buzzed in