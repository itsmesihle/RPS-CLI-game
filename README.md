# Rock Paper Scissors Game

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Course](https://img.shields.io/badge/Harvard-CS50P-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![Repo Size](https://img.shields.io/github/repo-size/itsmesihle/RPS-CLI-Game)
![Last Commit](https://img.shields.io/github/last-commit/itsmesihle/RPS-CLI-Game)
![Issues](https://img.shields.io/github/issues/itsmesihle/RPS-CLI-Game)

A clean, modular, and fully logged Rock–Paper–Scissors game written in **Python**. This project demonstrates professional OOP principles, architectural separation, automated testing, file handling and output logging, and input validation.

---

## 📚 Table of Contents

- [Project Description](#-project-description)
- [System Architecture](#-system-architecture)
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

This is a console-based Rock–Paper–Scissors game which welcomes the user with ASCII-art. The user is then prompted to select the number of rounds they would like to play:

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

## 🏗️ **System Architecture**

The project built using a **Layered Orchestration** and follows a modular design, ensuring that game logic is entirely decoupled from user interface and data persistence.

| Layer            | Class             | Responsibility                                               |
| :--------------- | :---------------- | :----------------------------------------------------------- |
| **Orchestrator** | `GameEngine`      | The "Brain" that coordinates the UI, Logic, and Data.        |
| **Core Logic**   | `RPSGame`         | Handles pure game rules, win/loss math, and move validation. |
| **Data**         | `GameDataManager` | Manages CSV initialization and persistent logging.           |
| **UI**           | `WelcomeMessage`  | Manages ASCII art and terminal presentation.                 |
| **Model**        | `GameRound`       | A lightweight container for storing round-specific data.     |

---

## 🎯 Why This Project Matters

This project demonstrates my ability to write testable, maintainable Python code while following good software engineering practices such as modularization, logging, and automated testing.

---

## 🧠 **Skills Showcased**

### **Object-Orientated Programming**

- **Encapsulation 💊:** Grouping related data and methods into classes to reduce global state.

- **Static Methods 🧮:** Using `@staticmethod` for pure logic (determining a winner) that doesn't rely on instance data.

- **Separation of Concerns 🧱:** Dividing the project into UI, Logic, and Storage layers.

### **Defensive Programming & Reliability**

- **Input Validation ⚠️:** Robust while True loops and try/except blocks to handle non-integer inputs and invalid moves.

- **Session Integrity 📑:** Implemented custom logic to log "aborted" status when a user exits mid-session via the 'q' command, ensuring data consistency in logs.

- **Cross-Platform Support 🔌:** Dynamic terminal clearing logic for both Windows (cls) and Unix/Mac (clear).

### **Software Engineering Best Practices**

- **Automated Testing 🧪:** Unit tests using pytest to verify the logic layer.

- **Data Persistence 📂:** Programmatic file I/O handling with the csv module, including automatic header initialization.

- **Version Control 🌿:** Managing code changes with Git and Github.

### **Soft Skills Demonstrated**

- **Code Documentation 📝:** Writing clear READMEs and docstrings to ensure that the "why" behind the code is just as obvious as the "how," making onboarding easier for other developers.

- **Code readability & maintainability 👓:** Prioritizing clean naming conventions and modular structure so the codebase remains easy to navigate and update long after the initial build.

---

## 🧩 **Technical Challenges & Solutions**

### 1. **Architecting for Scalability: From Procedural to Modular OOP**

My initial implementation of the game began as a single procedural script where logic, file I/O, and UI were all tightly coupled. This created a brittle environment where changing a simple data-saving rule risked breaking the entire application flow. To address this, I refactored the codebase into a modular, object-oriented architecture centered on the Separation of Concerns. By isolating responsibilities into specialized classes; a `GameDataManager` for file I/O, a `WelcomeMessage` for UI, and a `RPSGame` for core rules. I transformed a simple script into a scalable system. This Orchestration Layer now allows for seamless future upgrades, such as migrating from CSV to a SQLite database, without ever compromising the integrity of the underlying game logic.

### 2. Achieving 100% Testability Through Decoupling

A significant hurdle in the early development phase was the high degree of coupling between the game’s mathematical logic and its terminal-based display. Because `input()` prompts and `print()` statements were embedded directly within the game rules, the engine was "blindly" dependent on a human presence, making automated testing with `pytest` impossible. I resolved this by extracting all terminal interactions into the UI layer and refactoring the `RPSGame` class into a collection of pure functions. By ensuring the logic layer only accepts arguments and returns values, I achieved 100% test coverage. The system can now be verified instantly through automated scripts, ensuring the core engine remains robust regardless of how the user interface evolves.

### 3. Data Integrity and Graceful Termination

One of the more nuanced challenges involved handling user exits; specifically, ensuring that session data wasn't lost when a player used the `q` command to quit. Originally, the exit logic bypassed the data-logging routines, resulting in "dangling" sessions and incomplete history logs. I addressed this by implementing a formalized "aborted" state within the GameRound model. This allows the system to catch a quit signal as a valid lifecycle event, triggering a graceful shutdown that timestamps and logs the final state to the CSV before termination. This focus on data integrity ensures a reliable and complete audit trail for every user session, regardless of how the game ends..

---

## 📦 **Libraries & Modules Used**

- `random` – Computer move randomization.

- `csv & os` – Persistent data storage and file path management.

- `datetime` – Generating precise game-session timestamps.

- `pyfiglet` – Renders high-quality ASCII titles.

- `pytest` – Unit testing the logic layer.

---

## 🏗 **Project Structure**

```
.
├── project.py              # Main Application (class definitions & entry points)
├── requirements.txt        # External dependencies (pytest, pyfiglet)
├── RPS_game_data.csv       # Automatically generated game logs
├── test_project.py         # Automated tests
└── README.md               # Documentation of project
```

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

## 📝 **Project Roadmap**

This RPS game is still being worked on, constantly being updated

### **Past Improvements**

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
