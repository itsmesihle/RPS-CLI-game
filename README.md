# Rock Paper Scissors Game

A clean, modular, and fully logged Rock–Paper–Scissors game written in **Python**, featuring:

- User vs Computer CLI gameplay
- Score tracking
- CSV game-logging with timestamps
- Terminal ASCII-art welcome screen
- Input validation & robust structure

This project demonstrates beginner–intermediate Python fundamentals and is suitable for CS50P learners or anyone practicing Python structure and file handling -> THIS NEEDS TO BE WORKED ON ASAP!!

---

## 📌 **Project Description**

This is a console-based Rock–Paper–Scissors game where the welcomes the user with ASCII-art:

- _insert example_

The user is then prompted to select the number of rounds they would like to play:

- _insert example_

At this point the user is asked to select either rock, paper or scissors:

- **(r)** rock
- **(p)** paper
- **(s)** scissors

The computer randomly selects one of the three options, after which:

- The winner is determined
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

Manual install with:
`bash\pip install pyfiglet`

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

- uses Pytest to test the working order of the functions project.py by importing its modules
- _add more descriptive_

### **`README.md`**

- Contains documentation of the project.

---

## ▶️ **How to Run the game, and the tests**

### **Option A: automatic install**

1. _how to automatically install_:

```bash
insert code
```

2. Run the game:

```bash
python project.py
```

3. Run the tests:

```bash
pytest test_project.py
```

### **Option B: manual install**

1. Install Python (≥3.8)
2. Install dependencies:

```bash
pip install pyfiglet
```

3. Run the game:

```bash
python project.py
```

4. Run the tests:

```bash
pytest test_project.py
```

---

## 📝 **Status of Project**

This RPS game is still being worked on, constantly being updated

### 📝 **Future Improvements**

- Add difficulty modes
- Add analytics dashboard from CSV
- Add persistent user profiles
- Replace ASCII-art with animation

---

## 🤝 **Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please ensure your updates include:

Clear descriptions

Clean code formatting

Explanatory comments when needed

---

## 🐛 **Issues**

If you encounter bugs, crashes, or unexpected behavior, feel free to open an Issue on the repository. Please include:

Steps to reproduce

Expected vs actual behavior

Screenshots or logs (if applicable)

---

## 📄 **License**

This project is licensed under the MIT License - you are free to use, modify, and distribute it.

---

## 🙌 **Credits**

Created by **Sihle - @itsmesihle**, showcasing skills learnt through the Harvard University's CS50P course in a structured, logged, and playful Python application.
