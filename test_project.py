import pytest
# import class instead of function
from project import RPSGame

@pytest.fixture
def game():
    return RPSGame()

def test_determine_winner(game):
    assert game.determine_winner("r", "r") == "draw"
    assert game.determine_winner("p", "p") == "draw"
    assert game.determine_winner("s", "s") == "draw"

    assert game.determine_winner("r", "s") == "user"
    assert game.determine_winner("p", "r") == "user"
    assert game.determine_winner("s", "p") == "user"

    assert game.determine_winner("s", "r") == "computer"
    assert game.determine_winner("r", "p") == "computer"
    assert game.determine_winner("p", "s") == "computer"

def test_choice_integrity(game):
    # great thing about classes is that we can reach into the class and using an function that doesnt exist in the main file, to test an attribute of the class
    assert game.CHOICES['r'] == "rock"
    assert game.CHOICES['p'] == "paper"
    assert game.CHOICES['s'] == "scissors"
    assert len(game.CHOICES) == 3

