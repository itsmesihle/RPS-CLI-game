"""
DATABASE MANAGER for Rock-Paper-Scissors CLI
--------------------------------------------
Purpose:
This module handles all persistent data storage for the game using SQLite3.
It separates the "Data Logic" from the "Game Logic" (project.py).

Responsibilities:
1. Initialize the SQLite database and create necessary tables.
2. Provide functions to Create, Read, and Update player statistics.
3. Ensure data integrity (e.g., preventing duplicate usernames).

Why separate this?
By keeping SQL queries here, project.py remains clean and focused only 
on game flow and user interaction.
"""

import sqlite3