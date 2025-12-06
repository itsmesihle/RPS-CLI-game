# Rock Paper Scissors Game

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

A clean, modular, and fully logged Rock–Paper–Scissors game written in **Python**, featuring:

- User vs Computer CLI gameplay
- Score tracking
- CSV game-logging with timestamps
- Terminal ASCII-art welcome screen
- Input validation & robust structure

This project demonstrates solid beginner-to-intermediate Python skills, including modular design, input validation, file handling, and automated testing with pytest.

---

## 📌 **Project Description**

This is a console-based Rock–Paper–Scissors game where the welcomes the user with ASCII-art. The user is then prompted to select the number of rounds they would like to play:

![An image of ASCII-art when starting the game](<./images/Screenshot%20(782).png> "ASCII-art welcome")

At this point the user is asked to select either rock, paper or scissors:

- **(r)** rock
- **(p)** paper
- **(s)** scissors

The computer randomly selects one of the three options, after which:

- The winner is determined

![Winner is determined](<./images/Screenshot%20(783).png> "Winner is determined")

- The round is logged with timestamp, scores and results into `RPS_game_data.csv`

After the set number of rounds, a final scoreboard summary is displayed. After which the `RPS_game_date.csv` is saved, closed and stored on the local computer.

---

## 🧠 **Skills Showcased**

### **Python Fundamentals**

- Functions & modular programming
- Conditionals & loops
- Error handling with `try`/`except`
- User input validation
- Working with external libraries
- Use of the `__name__ == "__main__"` guard

### **Intermediate Concepts**

- File handling (CSV reading/writing)
- Logging data with timestamps
- Using 3rd‑party modules (`pyfiglet`)
- Clean code structuring
- Separation of concerns in functions

### **Soft Skills Demonstrated**

- Documentation
- Code readability & maintainability
- Defensive programming

---

## 📦 **Libraries & Modules Used**

### **Standard Library**

- `random` – computer choice
- `csv` – game data logging
- `datetime` – timestamp generation
- `os` – file checking
- `json` – used in development/testing

### **Third-Party Libraries**

- **pyfiglet** → ASCII‑art title screen
- **pytest** → unit-testing

---

## 🏗 **Project Structure**

```
.
├── project.py
├── requirements.txt
├── RPS_game_data.csv
├── test_project.py
└── README.md
```

### `project.py`

Contains all game logic:

- User prompts
- Computer randomization
- Winner determination
- CSV logging
- Scoreboard output

### `requirements.txt`

Contains all the requirements, dependencies necessary to run the game and the tests:

- Python (>3.8)
- Pyfiglet
- Pytest

### `RPS_game_data.csv`

Stores:

- Timestamp
- User choice
- Computer choice
- Round result

### **`test_project.py`**

This file contains the automated test suite for the project, written using pytest.
It validates:

- Winner logic
- Draw conditions
- Losing conditions

Additional tests can be added for CSV logging and input validation.

### **`README.md`**

- Contains documentation of the project.

---

## ▶️ **How to Run the game, and the tests**

1. Navigate to your project:

```bash
cd path/to/your/project
```

2. Install or update Python (≥3.8) on Windows:

```bash
# --- Install Python ---

winget install Python.Python.3
```

OR

```bash
# --- Upgrade Python ---

winget upgrade Python.Python.3
```

3. Install dependencies:

```bash
# --- Automatically install using requirements.txt ---

pip install -r requirements.txt
```

OR

```bash
# --- Manually install ---

pip install pyfiglet pytest
```

4. Run the game:

```bash
python project.py
```

5. Run the tests:

```bash
pytest test_project.py
```

---

## 📝 **Status of Project**

This RPS game is still being worked on, constantly being updated

### **Future Improvements**

- Add timeout function similar to setTimeout() in JS, that automatically quits if user is inactive
- ASCII-art disappears after 5 seconds on the terminal (the system in the background clears the screen after x seconds)
- Add difficulty modes
- Add a graphical UI (Tkinter or web-based)
- Add analytics dashboard from CSV
- Add persistent user profiles
- Replace ASCII-art with animated output
- Refactor logic for greater testability

---

## 🤝 **Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure your updates include:

- Clear descriptions
- Clean code formatting
- Explanatory comments when needed
- Please ensure your code passes all existing tests using pytest

---

## 🐛 **Issues**

If you encounter bugs, crashes, or unexpected behavior, feel free to open an Issue on the repository.

Please include:

- Steps to reproduce
- Expected vs actual behavior
- Screenshots or logs (if applicable)
- Python version

---

## 📄 **License**

This project is licensed under the MIT License - you are free to use, modify, and distribute it.

---

## 🙌 **Credits**

Created by **Sihle Ndlovu - @itsmesihle**

This project showcases concepts learned in Harvard’s CS50P course through a structured, logged, and test-driven Python application.
