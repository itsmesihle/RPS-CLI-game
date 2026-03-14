# Rock Paper Scissors Game

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Course](https://img.shields.io/badge/Harvard-CS50P-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Repo Size](https://img.shields.io/github/repo-size/itsmesihle/RPS-CLI-Game)
![Last Commit](https://img.shields.io/github/last-commit/itsmesihle/RPS-CLI-Game)
![Issues](https://img.shields.io/github/issues/itsmesihle/RPS-CLI-Game)

A clean, modular, and fully logged Rock–Paper–Scissors game written in **Python**, featuring:

- User vs Computer CLI gameplay
- Score tracking
- CSV game-logging with timestamps
- Terminal ASCII-art welcome screen
- Input validation & robust structure

This project demonstrates solid beginner-to-intermediate Python skills, including modular design, input validation, file handling, and automated testing with pytest.

---

## 📚 Table of Contents

- [Project Description](#-project-description)
- [Why This Project Matters](#-why-this-project-matters)
- [Skills Showcased](#-skills-showcased)
- [Libraries & Modules Used](#-libraries--modules-used)
- [Project Structure](#-project-structure)
- [How to Run](#️-how-to-run-the-game-and-the-tests)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [Issues](#-issues)
- [License](#-license)
- [Author & Attribution](#-author--attribution)
- [Connect with Me](#-connect-with-me)

---

## 📌 **Project Description**

This is a console-based Rock–Paper–Scissors game where the welcomes the user with ASCII-art. The user is then prompted to select the number of rounds they would like to play:

![An image of the ASCII-art welcome screen.](<./images/Screenshot%20(782).png> "ASCII-art welcome")

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

## 🎯 Why This Project Matters

This project demonstrates my ability to write testable, maintainable Python code while following good software engineering practices such as modularization, logging, and automated testing.

---

## 🧠 **Skills Showcased**

![Skills](https://img.shields.io/badge/Skills-Modular_Design%2C_Pytest%2C_File_I%2FO-orange)

### **Python Fundamentals**

- Functions & modular code 🧩
- Loops & conditionals 🌀

### **Object-Orientated Programming**

- Encapsulation: Grouping related data and methods into classes to reduce global state.

- Static Methods: Using `@staticmethod` for pure logic (determining a winner) that doesn't rely on instance data.

- Separation of Concerns: Dividing the project into UI, Logic, and Storage layers.

### **Intermediate Concepts**

- File I/O 📂: Programmatic creation and appending of CSV files
- Error handling ⚠️: robust `try/except` blocks for user input validation
- Cross-Platform Support 🧩: Logic to handle terminal clearing on both Windows (`cls`) and Linux/Mac (`clear`).

### **Soft Skills Demonstrated**

- Code Documentation 📝
- Code readability & maintainability 👓
- Defensive programming 🛡️

---

## 📦 **Libraries & Modules Used**

- `random` – Computer move randomization.

- `csv & os` – Persistent data storage and file path management.

- `datetime` – Generating precise game-session timestamps.

- `pyfiglet` – Renders high-quality ASCII titles.

- `pytest` – Unit testing the logic layer.

## 🏗 **Project Structure**

```
.
├── project.py              # Main Application
├── requirements.txt        # External dependencies
├── RPS_game_data.csv       # Automatically generated game logs
├── test_project.py         # Automated tests
└── README.md               # Documentation
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

Contains documentation of the project.

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

⏳ Gameplay Improvements

- Away From Keyboard timeout function
- Auto-hide ASCII-art

🎮 Feature Additions

- Difficulty modes, implement a simple algorithm that tracks user patterns
- Transition the UI layer from CLI to a graphical interface using Tkinter or PyQt.

📊 Data & Analytics

- CSV dashboard with "Win Rate" report
- Machine learning

Testing

- Implement coverage.py and ensure coverage of < 90%
- make use of properties

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

## 🙌 **Author & Attribution**

Created by **Sihle Ndlovu - @itsmesihle**

This project demonstrates the transition from a functional script to a scalable, class-based application, following clean code principles learned in Harvard’s CS50P.

---

## 👋 **Connect with Me**

I am a job seeker actively looking for **Software Developer** or **Backend Python** opportunities.

This project demonstrates my proficiency in building **testable, modular Python applications**.

I welcome connection requests from recruiters and fellow developers to discuss:

- This project and the technical decisions made.
- Potential full-time roles or internships.

### **Let's Connect!**

- 🔗 [LinkedIn](https://www.linkedin.com/in/itsmesihle/)
- 📧 [Email](mailto:msihlesndlovu97@gmail.com?subject=Let's%20Connect%20-%20RPS%20-%20Game)
- 💻 [Portfolio](https://github.com/itsmesihle)
