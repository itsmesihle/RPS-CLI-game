import sqlite3
import random
import os
from datetime import datetime
from pyfiglet import Figlet

class GameRound:
    """Model layer representing the outcome of a single round with validation."""
    VALID_WINNERS = {"user", "computer", "draw", "aborted"}

    def __init__(self, user, computer, winner):
        self.user = user
        self.computer = computer
        self.winner = winner  # Triggers our property validation below

    @property
    def winner(self):
        return self._winner

    @winner.setter
    def winner(self, value):
        if value not in self.VALID_WINNERS:
            raise ValueError(f"Invalid winner status: {value}. Must be one of {self.VALID_WINNERS}")
        self._winner = value

# 1. DATA HANDLING LAYER
class GameDataManager:
    """Manages the sqlite3 database for persistent game history"""
    def __init__(self, db_name="../data/rps_history.db"):
        self.db_name = db_name
        self._initialize_db()

    def _initialize_db(self):
        """Creates the results table if it doesn't already exist"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
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
            print(f"Database Initialization Error: {e}")

    def log_result(self, round_data):
        """Saves a single round's data into the SQLite database."""
        timestamp = datetime.now().isoformat(timespec="seconds")
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO game_results (timestamp, user_choice, computer_choice, winner)
                    VALUES (?, ?, ?, ?)
                ''', (timestamp, round_data.user, round_data.computer, round_data.winner))
                conn.commit()
        except sqlite3.Error as e:
            print(f"Failed to log result: {e}")

# 2. UI LAYER
class GameUI:
    """Handles visual presentation and console input/output parsing."""
    def __init__(self, font='xsansb'):
        self.figlet = Figlet(font=font)
        self.choices = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_user_choice(self):
        """Gets user input and validates it against valid choices."""
        while True:
            move = input("Choose between (r/p/s): ").lower().strip()
            if move == 'q' or move in self.choices:
                return move
            print("\nInvalid input! please try again")

    def get_number_of_rounds(self):
        """Initializes game setup by requesting game count."""
        while True:
            n = input("How many games would you like to play? ").lower().strip()
            if n == 'q': 
                print("Thanks for playing.")
                return None  # Explicitly returning None to handle exits gracefully
            try:
                rounds = int(n)
                if rounds > 0: 
                    return rounds
                print("Enter a positive number. ")
            except ValueError:
                print("Invalid input. Enter a number")

    def _clear_terminal(self):
        """Wipes the terminal screen based on the operating system."""
        command = "cls" if os.name == "nt" else "clear"
        os.system(command)

    def display_ascii(self):
        """Displays ASCII art header."""
        self._clear_terminal()
        print(self.figlet.renderText('Rock. Paper. Scissors.'))
        print("Press 'q' at ANY TIME to quit.\n")

# 3. LOGIC LAYER
class RPSGame:
    """Pure mathematical logic of game mechanics entirely decoupled from I/O."""
    CHOICES = {"r": "rock", "p": "paper", "s": "scissors"}

    def get_computer_choice(self):
        return random.choice(list(self.CHOICES.keys()))
    
    @staticmethod
    def determine_winner(user, computer):
        """Evaluates choices and evaluates rules to return winner state."""
        if user == computer:
            return "draw"
        win_conditions = [('r', 's'), ('s', 'p'), ('p', 'r')]
        if (user, computer) in win_conditions:
            return "user"
        return "computer"
    
    def play_single_round(self, user_choice=None):
        """Plays 1 round of RPS and returns calculated GameRound model status."""
        if user_choice is None or user_choice == 'q':
            return GameRound(user='q', computer=None, winner='aborted')
        
        comp_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, comp_choice)
        return GameRound(user_choice, comp_choice, winner)

# 4. ORCHESTRATION LAYER
class GameEngine:
    """Orchestrates layout layer logic workflow using dependency injection."""
    def __init__(self, data_manager, ui_layer, game_logic):
        self.data = data_manager
        self.ui = ui_layer
        self.engine = game_logic
        self.user_score = 0
        self.computer_score = 0

    def start(self):
        self.ui.display_ascii()
        rounds = self.ui.get_number_of_rounds()

        if rounds is None:  # Fixed the hidden string matching type bug cleanly!
            return 

        for i in range(rounds):
            print(f"\nRound {i + 1} of {rounds}")
            move = self.ui.get_user_choice()
            
            current_round = self.engine.play_single_round(move)
            self.data.log_result(current_round)

            if current_round.winner == 'aborted':
                print("Game aborted by user")
                break

            self._process_round_result(current_round)

        self._display_final_score()

    def _process_round_result(self, round_data):
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
    # Instantiate layers cleanly and inject them down into the engine
    db_manager = GameDataManager()
    ui_display = GameUI()
    core_logic = RPSGame()
    
    game = GameEngine(data_manager=db_manager, ui_layer=ui_display, game_logic=core_logic)
    game.start()