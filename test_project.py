import pytest
from main import determine_winner

def test_determine_winner():
    assert determine_winner("r", "r") == "draw"
    assert determine_winner("p", "p") == "draw"
    assert determine_winner("s", "s") == "draw"

    assert determine_winner("r", "s") == "user"
    assert determine_winner("p", "r") == "user"
    assert determine_winner("s", "p") == "user"

    assert determine_winner("s", "r") == "computer"
    assert determine_winner("r", "p") == "computer"
    assert determine_winner("p", "s") == "computer"


