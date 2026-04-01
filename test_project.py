import pytest
import random
# import class instead of function
from project import RPSGame, GameRound, GameDataManager

@pytest.fixture
def game():
    return RPSGame()

# UNIT TEST: logic validation
def test_determine_winner(game):
    """verifies core rules of the game"""

    assert game.determine_winner("r", "r") == "draw"
    assert game.determine_winner("p", "p") == "draw"
    assert game.determine_winner("s", "s") == "draw"

    assert game.determine_winner("r", "s") == "user"
    assert game.determine_winner("p", "r") == "user"
    assert game.determine_winner("s", "p") == "user"

    assert game.determine_winner("s", "r") == "computer"
    assert game.determine_winner("r", "p") == "computer"
    assert game.determine_winner("p", "s") == "computer"

# UNIT TEST: attribute validation
def test_choice_integrity(game):
    """ensures integrity and consistency of computer choices."""
    # great thing about classes is that we can reach into the class and using an function that doesnt exist in the main file, to test an attribute of the class

    assert game.CHOICES['r'] == "rock"
    assert game.CHOICES['p'] == "paper"
    assert game.CHOICES['s'] == "scissors"
    assert len(game.CHOICES) == 3

# UNIT TEST: edge case
def test_play_single_round_aborted(game):
    """tests the 'exit' logic """

    result = game.play_single_round('q')
    assert result.winner == 'aborted'
    assert result.user == 'q'
    assert result.computer is None

# SYSTEM/IO TEST: csv file validation
def test_csv_initialization(tmp_path):
    """tests if the data layer correctly interacts with the file system
    Note: tmp_path is pytest fixture which creates a temporary directory
    """

    # creates a fake path inside temp folder
    test_file = tmp_path / "RPS_game_data.csv"

    # initializes the manager with the fake path
    manager = GameDataManager(filename=str(test_file))

    # tests if the file was created
    assert test_file.exists()

    # check if the headers are correct?
    with open(test_file, "r") as f:
        header = f.readline().strip()
        assert header == "timestamp,user_choice,computer_choice,winner"
