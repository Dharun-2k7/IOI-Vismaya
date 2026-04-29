import sqlite3

def update_schema():
    conn = sqlite3.connect('instance/site.db')
    c = conn.cursor()
    
    try:
        c.execute("ALTER TABLE user ADD COLUMN current_streak INTEGER DEFAULT 0")
        print("Added current_streak")
    except sqlite3.OperationalError as e:
        print(f"current_streak: {e}")
        
    try:
        c.execute("ALTER TABLE user ADD COLUMN longest_streak INTEGER DEFAULT 0")
        print("Added longest_streak")
    except sqlite3.OperationalError as e:
        print(f"longest_streak: {e}")
        
    try:
        c.execute("ALTER TABLE user ADD COLUMN last_solve_date DATE")
        print("Added last_solve_date")
    except sqlite3.OperationalError as e:
        print(f"last_solve_date: {e}")
        
    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_schema()
