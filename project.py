import csv
import random
import os
from datetime import datetime
from pyfiglet import Figlet
# from threading import Timer

# I am thinking that this code needs 2 main classes
# 1. playing the actual game
# 2. logging the results to csv

class GameManager: # manages the csv file and management of it

    def __init__(self, filename="RPS_game_data.csv"):
        self.filename = filename
        self._initialize_csv()

    def _initialize_csv(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            with open(self.filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["timestamp", "user_choice", "computer_choice", "winner"])

    def log_result_to_csv(self, user_choice, computer_choice, winner):
        timestamp = datetime.now().isoformat(timespec="seconds")
        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp, user_choice, computer_choice, winner])

def main():

    # welcome procedure
    print_welcome_message()
    total_rounds = get_valid_number_of_rounds("How many games would you like to play? ")

    # declare variables
    user_score = 0
    computer_score = 0
    rounds_played = 0

    # actual game plays
    while rounds_played < total_rounds:
        print(f"\nRound {rounds_played + 1} of {total_rounds}")

        # get user choice OR abort sequence
        user_choice = get_user_choice()

        if user_choice == "QUIT_GAME":
            print("\n Game is aborted early.")
            log_to_csv("quit", "-", "aborted")
            break

        # INVALID CHOICE handling
        valid_options = ["r", "p", "s"]
        if user_choice not in valid_options:
            print("\nInvalid choice. Please type 'r', 'p' or 's'. \n")
            log_to_csv(user_choice, "-", "invalid")
            continue

        # get computer choice
        computer_choice = get_computer_choice()

        #change user and computer choices into words for output purposes
        user_word = choice_to_word(user_choice)
        computer_word = choice_to_word(computer_choice)

        # determine winner
        winner = determine_winner(user_choice, computer_choice)

        # logs to csv
        log_to_csv(user_choice, computer_choice, winner)

        # tally score
        if winner == "draw":
            # increment both scores
            print(f"You and the computer both picked {user_word}. Its a draw! play again. ")
            continue

        elif winner == "invalid":
            print(f"That was an invalid choice. ")
            continue

        elif winner == "user":
            print(f"You chose {user_word} and the computer chose {computer_word}. You win this round!")
            user_score += 1

        elif winner == "computer":
            print(f"You chose {user_word} and the computer chose {computer_word}. Computer won this round!")
            computer_score += 1

        rounds_played += 1

    # display final score...close
    get_score(computer_score, user_score)

def print_welcome_message():
    show_ascii()

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_ascii():
    f = Figlet(font='xsansb')
    print("\nLet's play\n")
    print(f.renderText('Rock. Paper. Scissors.'))
    print("Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.\n")
    print("Press 'q' at ANY TIME to quit the game\n")
    Timer(5.0, clear_screen).start()

def get_valid_number_of_rounds(prompt):
    # gets valid int to determine how many rounds will be played
    while True:
        user = input(prompt).lower().strip()
        if user == "q":
            print("\nGame aborted before starting.")
            log_to_csv("quit", "-", "aborted")
            exit()

        try:
            n = int(user)
            if n > 0:
                return n
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. please enter a number")

def safe_input(prompt=""):
    user = input(prompt).lower().strip()
    if user == "q":
        print("\nGame aborted by user.")
        return "QUIT_GAME"
    return user

def get_user_choice():
    choice = input("Choose between (r)ock, (p)aper or (s)cissors or 'q' to quit: ").lower().strip()
    if choice == "q":
        return "QUIT_GAME"
    return choice

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def choice_to_word(r):
    return {"r": "rock", "p": "paper", "s": "scissors"}.get(r, "?")

def determine_winner(user, computer):
    if user == computer:
        return "draw"

    elif (
        (user == "r" and computer == "s") or
        (user == "s" and computer == "p") or
        (user == "p" and computer == "r")):
        return "user"

    elif (
        (user == "r" and computer == "p") or
        (user == "s" and computer == "r") or
        (user == "p" and computer == "s")):
        return "computer"

    else:
        return "invalid"

def get_score(computer_score, user_score):
        print(f"\n--- Final Scores --- \n--- Computer Score: {computer_score}\n--- Your Score: {user_score}\n")
        if computer_score > user_score:
            print("The computer won...YOU SUCK!!!\n")
        elif computer_score == user_score:
            print("You and the computer are evenly matched. It's a DRAW!!!")
        else:
            print("Congrats you WON!!!\n")

if __name__ == "__main__":
    main()

