import sqlite3
import random
import os
from datetime import datetime
from pyfiglet import Figlet

class GameRound:
    def __init__(self, user, computer, winner):
        self.user = user
        self.computer = computer
        self.winner = winner

# 1. DATA HANDLING LAYER
class GameDataManager:
    """Manages the sqlite3 database for persistent game history"""
    def __init__(self, db_name="rps_history.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """creates the results table if it doesnt already exist"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Using schema
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS game_results(
                               id INTEGER PRIMARY KEY AUTOINCREMENT,
                               timestamp TEXT NOT NULL,
                               user_choice TEXT,
                               computer_choice TEXT,
                               winner TEXT NOT NULL
                               )
                ''')
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database Initialisation Error: {e}")

    def log_result(self, round_data):
        """Saves a single round's data into the SQLite database."""
        timestamp = datetime.now().isoformat(timespec="seconds")
        
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                # Security Best Practice: Using '?' placeholders to prevent SQL Injection
                cursor.execute('''
                    INSERT INTO game_results (timestamp, user_choice, computer_choice, winner)
                    VALUES (?, ?, ?, ?)
                ''', (timestamp, round_data.user, round_data.computer, round_data.winner))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to log result: {e}")

class GameUI:
    """2. UI Layer - handles visual presentation and ASCII art."""
    def __init__(self, font='xsansb'):
        self.figlet = Figlet(font=font)
        self.choices = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_user_choice(self):
        """Gets user input, validates it against CHOICES and returns user choice"""
        while True:
            move = input("Choose between (r/p/s): ").lower().strip()
            if move == 'q' or move in self.choices:
                return move
            print("\nInvalid input! please try again")

    def get_number_of_rounds(self):
        """UI Method to intialises game setup"""
        while True:
            n = input("How many games would you like to play? ").lower().strip()
            if n == 'q': 
                print("Thanks for playing.")
                return 
            try:
                rounds = int(n)
                if rounds > 0: 
                    return rounds
                print("Enter a positive number. ")
            except ValueError:
                print("Invalid input. Enter a number")

    def _clear_terminal(self):
        """Wipes the terminal screen based on the operating system"""
        command = "cls" if os.name == "nt" else "clear"
        os.system(command)

    def displayASCII(self):
        """displays ascii art"""
        self._clear_terminal()
        print(self.figlet.renderText('Rock. Paper. Scissors.'))
        print("Press 'q' at ANY TIME to quit.\n")

class RPSGame:
    """3. Logic Layer - pure logic of game lives here. no print() or input() logic here"""
    CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))
    
    @staticmethod # like a calculator, doesn't care whats inside the 
    def determine_winner(user, computer):
        """"checks win conditions for user, then returns 'user', 'computer' or 'draw'"""
        if user == computer:
            return "draw"
        win_conditions = [('r', 's'), ('s', 'p'), ('p', 'r')]
        if (user, computer) in win_conditions:
            return "user"
        return "computer"
    
    def play_single_round(self, user_choice):
        """play 1 round of RPS keep score of round, return GameRound with args as choices and winner"""

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
        self.ui = GameUI()
        self.engine = RPSGame()
        self.user_score = 0
        self.computer_score = 0

    def start(self):
        #display message
        self.ui.displayASCII()

        # 1. ask UI for number of rounds by calling function
        rounds = self.ui.get_number_of_rounds()

        if rounds == "q":
            print("Thanks for playing. ")
            return 

        for i in range(rounds):
            print(f"\nRound {i + 1} of {rounds}")
            # round is played and repeated inside loop
            current_round = self.engine.play_single_round()
            # LOG THE RESULT
            self.data.log_result(current_round)

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
            print(f"Draw! You both chose {u_name}")
        elif round_data.winner == "user":
            print(f"\nYou win! {u_name.capitalize()} beats {c_name}.")
            self.user_score += 1
        else:
            print(f"\n You lose! {c_name.capitalize()} beats {u_name}.")
            self.computer_score += 1

    def _display_final_score(self):
        print("\n" + "-" * 10 , " FINAL SCORE ", "-" *10)
        print(f"\nYou: {self.user_score} || CPU: {self.computer_score}")
        print("-" * 35)

if __name__ == "__main__":
    game = GameEngine()
    game.start()