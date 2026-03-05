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

class GameRound:
    def __init__(self, user, computer, winner):
        self.user = user
        self.computer = computer
        self.winner = winner

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

    def log_result_to_csv(self, round_data):
        timestamp = datetime.now().isoformat(timespec="seconds")
        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                timestamp, 
                round_data.user, 
                round_data.computer, 
                round_data.winner
                ])

# 2. USER INTERFACE LAYER
class WelcomeMessage:
    """Handles visual presentation and ASCII art."""
    def __init__(self, font='xsansb'):
        self.figlet = Figlet(font=font)

    def displayASCII(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(self.figlet.renderText('Rock. Paper. Scissors.'))
        print("Press 'q' at ANY TIME to quit.\n")

# 3. LOGIC LAYER
# pure logic of game lives here

class RPSGame:
    CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))
    
    def get_user_choice(self):
        """Gets user input and validates it"""
        while True:
            move = input("Choose between (r/p/s) or q to quit game: ").lower().strip()
            if move == 'q' or move in self.CHOICES:
                return move
            print("Invalid input! please try again")
    
    @staticmethod # like a calculator, doesn't care whats inside the 
    def determine_winner(user, computer):
        if user == computer:
            return "draw"
        win_conditions = [('r', 's'), ('s', 'p'), ('p', 'r')]
        if (user, computer) in win_conditions:
            return "user"
        return "computer"
    
    def play_single_round(self):
        user_choice = self.get_user_choice()
        comp_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, comp_choice)

        # handle 'q' scenario...quit immediately
        if user_choice == 'q':
            return GameRound(user='q', computer=None, winner='aborted')
        
        return GameRound(user_choice, comp_choice, winner)

# 4. ORCHESTRATION LAYER or THE ENGINE (where everything works together)
class GameEngine:
    def __init__(self):
        self.data = GameDataManager()
        self.ui = WelcomeMessage()
        self.engine = RPSGame()
        self.user_score = 0
        self.computer_score = 0

    def start(self):
        #display message
        self.ui.displayASCII()

        # int input validation
        n = input("How many games would you like to play? ").lower().strip()
        if n == 'q': 
            return GameRound(user='q', computer=None, winner='aborted')
        try:
            rounds = int(n)
            if rounds > 0: 
                return
            print("Enter a positive number. ")
        except ValueError:
            print("Invalid input. Enter a number")

        for i in range(rounds):
            print(f"\nRound {i + 1} of {rounds}")
            # round is played and repeated inside loop
            current_round = self.engine.play_single_round()
            # LOG THE RESULT
            self.data.log_result_to_csv(current_round)

            # check if we need to break loop
            if current_round.winner == 'aborted':
                print("Game aborted by user")
                break

            # process visual feedback and score
            self._process_round_result(current_round)
        self._display_final_score()

    def _process_round_result(self, round_data):
        # updates scores and prints the outcome of a completed round
        u_name = self.engine.CHOICES[round_data.user]
        c_name = self.engine.CHOICES[round_data.computer]

        if round_data.winner == "draw":
            print(f"Draw! Both chose {u_name}")
        elif round_data.winner == "user":
            print(f"Win! {u_name} beats {c_name}.")
            self.user_score += 1
        else:
            print(f"Loss! {c_name} beats {u_name}.")
            self.computer_score += 1

    def _display_final_score(self):
        print("\n", "-" * 10 , " FINAL SCORE ", "-" *10)
        print(f"\nYou: {self.user_score} || CPU: {self.computer_score}")
        print("-" * 30)

if __name__ == "__main__":
    game = GameEngine()
    game.start()