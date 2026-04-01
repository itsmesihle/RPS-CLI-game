import csv
import sqlite3
from datetime import datetime

# Configuration
CSV_FILE = "RPS_game_data.csv"
DB_FILE = "rps_history.db"

def migrate_data():
    try:
        # 1. Connect to the new database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # 2. Ensure the table exists (Schema)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                user_choice TEXT,
                computer_choice TEXT,
                winner TEXT NOT NULL
            )
        ''')

        # 3. Open and read the CSV
        with open(CSV_FILE, mode='r') as f:
            reader = csv.DictReader(f) # DictReader uses the header row as keys
            
            # Prepare the data for batch insertion
            to_db = [
                (row['timestamp'], row['user_choice'], row['computer_choice'], row['winner'])
                for row in reader
            ]

        # 4. Insert data using 'executemany' (High Performance)
        cursor.executemany('''
            INSERT INTO game_results (timestamp, user_choice, computer_choice, winner)
            VALUES (?, ?, ?, ?)
        ''', to_db)

        conn.commit()
        print(f"Successfully migrated {len(to_db)} rounds to {DB_FILE}!")

    except FileNotFoundError:
        print(f"Error: {CSV_FILE} not found. Nothing to migrate.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate_data()