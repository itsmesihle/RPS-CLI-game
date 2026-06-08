import sqlite3
from datetime import datetime

def view_history():
    db_name = "rps_history.db"
    
    try:
        # 1. Connect to the database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # 2. Fetch the latest 10 rounds
        cursor.execute("SELECT id, timestamp, user_choice, computer_choice, winner FROM game_results ORDER BY id DESC LIMIT 10")
        rows = cursor.fetchall()

        if not rows:
            print("\n[!] No game history found in the database.")
            return

        # 3. Print a formatted header
        print(f"\n{'ID':<4} | {'Date & Time':<20} | {'User':<8} | {'ComputerS':<8} | {'Winner':<10}")
        print("-" * 60)

        # 4. Loop through and print rows
        for row in rows:
            # Formatting the timestamp for readability
            dt = datetime.fromisoformat(row[1]).strftime("%Y-%m-%d %H:%M")
            print(f"{row[0]:<4} | {dt:<20} | {row[2]:<8} | {row[3]:<8} | {row[4]:<10}")

        # 5. Show a quick summary
        cursor.execute("SELECT winner, COUNT(*) FROM game_results GROUP BY winner")
        stats = cursor.fetchall()
        
        print("\n--- Lifetime Stats ---")
        for stat in stats:
            print(f"{stat[0].capitalize()}: {stat[1]}")

    except sqlite3.OperationalError:
        print(f"\n[!] Error: Could not find table 'game_results'. Have you run a game yet?")
    finally:
        conn.close()

if __name__ == "__main__":
    view_history()