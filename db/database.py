# import sqlite3

# conn = sqlite3.connect("ielts.db", check_same_thread=False)
# cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS sessions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     mode TEXT,
#     transcript TEXT,
#     band_score REAL,
#     fluency REAL,
#     grammar REAL,
#     vocab REAL,
#     pronunciation REAL,
#     feedback TEXT,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# conn.commit()


import sqlite3

DB_NAME = "app.db"

def get_db():
    return sqlite3.connect(DB_NAME, check_same_thread=False)
