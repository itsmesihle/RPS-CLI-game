import csv
import random
import os
from datetime import datetime
from pyfiglet import Figlet
# from threading import Timer

# I am thinking that this code needs 4 main classes
# 1. data layer (csv)
# 2. ui layer (welcome message)
# 3. game logic
# 4. orchestrator class = engine of the game

# 1. DATA HANDLING LAYER
class GameDataManager: # manages the csv file
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

# 2. USER INTERFACE LAYER
class WelcomeMessage:
    """Handles visual presentation and ASCII art."""
    def __init__(self, font='xsansb'):
        self.figlet = Figlet(font=font)

    def displayASCII(self):
        print(self.figlet.renderText('Rock. Paper. Scissors.'))
        print("Press 'q' at ANY TIME to quit.\n")

# 3. LOGIC LAYER
# pure logic of game lives here

class RPSGame:
    CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))
    
    @staticmethod # like a calculator, doesnt care whats inside the 
    def determine_winner(user, computer):
        if user == computer:
            return "draw"
        win_conditions = [('r', 's'), ('s', 'p'), ('p', 'r')]
        if (user, computer) in win_conditions:
            return "user"
        return "computer"
    
# 4. ORCHESTRATION LAYER or THE ENGINE (where everything works together)
class GameEngine:
    def __init__(self):
        self.data = GameDataManager()
        self.ui = WelcomeMessage()
        self.engine = RPSGame()
        self.user_score = 0
        self.computer_score = 0

    def get_valid_rounds(self):
        while True:
            rounds = input("How many games would you like to play? ").lower().strip()
            if rounds == 'q': 
                return "QUIT_GAME"
            try:
                n = int(rounds)
                if n > 0: 
                    return n
                print("Enter a number > 0.")
            except ValueError:
                print("Invalid input. Enter a number")

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

def get_score(computer_score, user_score):
        print(f"\n--- Final Scores --- \n--- Computer Score: {computer_score}\n--- Your Score: {user_score}\n")
        if computer_score > user_score:
            print("The computer won...YOU SUCK!!!\n")
        elif computer_score == user_score:
            print("You and the computer are evenly matched. It's a DRAW!!!")
        else:
            print("Congrats you WON!!!\n")

if __name__ == "__main__":
    main = GameEngine()

