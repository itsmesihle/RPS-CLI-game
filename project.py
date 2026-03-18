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

class GameDataManager: 
    """1. Data Layer - manages the csv file data """
    def __init__(self, filename="RPS_game_data.csv"):
        self.filename = filename
        self._initialize_csv()

    def _initialize_csv(self):
        """checks if file exists or is empty in file path, then initialises it by writing headers at top of csv file"""
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            with open(self.filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["timestamp", "user_choice", "computer_choice", "winner"])

    def log_result_to_csv(self, round_data):
        """takes round_data as arg, creates timestamp and writes all of those into csv file"""
        timestamp = datetime.now().isoformat(timespec="seconds")
        with open(self.filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                timestamp, 
                round_data.user, 
                round_data.computer, 
                round_data.winner
                ])

class WelcomeMessage:
    """2. UI Layer - handles visual presentation and ASCII art."""
    def __init__(self, font='xsansb'):
        self.figlet = Figlet(font=font)

    def _clear_terminal(self):
        """Wipes the terminal screen based on the operating system"""
        command = "cls" if os.name == "nt" else "clear"
        os.system(command)

    def displayASCII(self):
        """displays ascii art"""
        self._clear_terminal()
        print(self.figlet.renderText('Rock. Paper. Scissors.'))
        print("Press 'q' at ANY TIME to quit.\n")

# 3. LOGIC LAYER
# pure logic of game lives here

class RPSGame:
    """Logic Layer - pure logic of game lives her"""
    CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))
    
    def get_user_choice(self):
        """Gets user input, validates it against CHOICES and returns user choice"""
        while True:
            move = input("Choose between (r/p/s): ").lower().strip()
            if move == 'q' or move in self.CHOICES:
                return move
            print("Invalid input! please try again")
    
    @staticmethod # like a calculator, doesn't care whats inside the 
    def determine_winner(user, computer):
        """"checks win conditions for user, then returns 'user', 'computer' or 'draw'"""
        if user == computer:
            return "draw"
        win_conditions = [('r', 's'), ('s', 'p'), ('p', 'r')]
        if (user, computer) in win_conditions:
            return "user"
        return "computer"
    
    def play_single_round(self):
        """play 1 round of RPS keep score of round, return GameRound with args as choices and winner"""
        user_choice = self.get_user_choice()

        """Checks for 'q' before calculating winner, if true log GameRound with args """
        if user_choice == 'q':
            return GameRound(user='q', computer=None, winner='aborted')
        
        comp_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, comp_choice)
        
        return GameRound(user_choice, comp_choice, winner)

class GameEngine:
    """  ORCHESTRATION LAYER - where everything works together"""
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
        rounds = 0
        while True:
            n = input("How many games would you like to play? ").lower().strip()
            if n == 'q': 
                print("Thanks for playing.")
                return 
            try:
                rounds = int(n)
                if rounds > 0: 
                    break
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

            self._process_round_result(current_round)

        """process visual feedback and score """
        self._display_final_score()

    def _process_round_result(self, round_data):
        """ updates scores and prints the outcome of a completed round """
        u_name = self.engine.CHOICES[round_data.user]
        c_name = self.engine.CHOICES[round_data.computer]

        if round_data.winner == "draw":
            print(f"Draw! Both chose {u_name}")
        elif round_data.winner == "user":
            print(f"Win! {u_name.capitalize()} beats {c_name}.")
            self.user_score += 1
        else:
            print(f"Loss! {c_name.capitalize()} beats {u_name}.")
            self.computer_score += 1

    def _display_final_score(self):
        print("\n" + "-" * 10 , " FINAL SCORE ", "-" *10)
        print(f"\nYou: {self.user_score} || CPU: {self.computer_score}")
        print("-" * 35)

if __name__ == "__main__":
    game = GameEngine()
    game.start()