from pyfiglet import Figlet
import pyfiglet
import json
import csv
import random
import os
from datetime import datetime

def main():
    # initiliaze csv
    initialize_csv()

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

        elif winner == "user":
            print(f"You chose {user_word} and the computer chose {computer_word}. You win this round!")
            user_score += 1

        elif winner == "computer":
            print(f"You chose {user_word} and the computer chose {computer_word}.Computer won this round!")
            computer_score += 1

        rounds_played += 1

    # display final score...close
    get_score(computer_score, user_score)

def initialize_csv():
    file_name = "RPS_game_data.csv"
    # Check path if file exists or empty, if not then create it
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(file_name, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["timestamp", "user_choice", "computer_choice", "winner"])

def print_welcome_message():
    f = Figlet(font='xsansb')
    print("\nLet's play\n")
    print(f.renderText('Rock. Paper. Scissors.'))
    print("Rock beats Scissors, Scissors beat Paper, and Paper beats Rock.\n")
    print("Press 'q' at ANY TIME to quit the game\n")

def get_valid_number_of_rounds(prompt):
    # gets valid int to determine how many rounds will be played
    while True:
        user = input(prompt).lower().strip()
        if user == "q":
            print("\n⚠️ Game aborted before starting.")
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
    valid_choices = ["r", "p", "s", "q"]
    while True:
        choice = input("Choose between (r)ock, (p)aper or (s)cissors or 'q' to quit: ").lower().strip()
        if choice == "q":
            return "QUIT_GAME"
        if choice in valid_choices:
            return choice
        else:
            print("\nInvalid choice. Please type 'r', 'p', 's' or 'q'.")

def get_computer_choice():
    return random.choice(["r", "p", "s"])

def choice_to_word(r):
    return {"r": "rock", "p": "paper", "s": "scissors"}.get(r, "?")

def determine_winner(user, computer):
    if user == computer:
        return "draw"

    elif (
        (user == "r" and computer == "s") or
        (user == "s" and computer == "r") or
        (user == "p" and computer == "r")):
        return "user"

    else:
        return "computer"

def log_to_csv(user_choice, computer_choice, winner):
    timestamp = datetime.now().isoformat(timespec="seconds")
    with open("RPS_game_data.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, user_choice, computer_choice, winner])

def get_score(computer_score, user_score):
        print(f"\n--- Final Scores --- \n--- Computer Score: {computer_score}\n--- Your Score: {user_score}\n")
        if computer_score > user_score:
            print("Unlucky the computer won...YOU SUCK!!!\n")
        elif computer_score == user_score:
            print("You and the computer are evenly matched. It's a DRAW!!!")
        else:
            print("Congrats you WON!!!\n")

if __name__ == "__main__":
    main()

""" # sorted fonts
font_list = pyfiglet.FigletFont.getFonts()
sorted_fonts = sorted(font_list)
readable_response = json.dumps(sorted_fonts, indent=4)

# print font and font example
example_text = 'Rock. Paper. Scissors. 123'

for font_name in sorted_fonts:
    f = Figlet(font=font_name)
    rendered_text = f.renderText(example_text)
    print(f"font name - {font_name}\n {rendered_text}")
#print(readable_response)
 """
