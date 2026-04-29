import sqlite3

def update_schema():
    conn = sqlite3.connect('instance/site.db')
    c = conn.cursor()
    
    try:
        c.execute("ALTER TABLE user ADD COLUMN last_solve_time DATETIME")
        print("Added last_solve_time")
    except sqlite3.OperationalError as e:
        print(f"last_solve_time: {e}")
        
    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_schema()
