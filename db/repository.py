import uuid
from db.database import get_db
from db.models import init_db

init_db()

def create_session():
    session_id = str(uuid.uuid4())
    db = get_db()
    db.execute("INSERT INTO sessions (id) VALUES (?)", (session_id,))
    db.commit()
    db.close()
    return session_id

def save_message(session_id, user, ai):
    db = get_db()
    db.execute(
        "INSERT INTO messages (session_id, user, ai) VALUES (?, ?, ?)",
        (session_id, user, ai)
    )
    db.commit()
    db.close()

def get_conversation(session_id):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT user, ai FROM messages WHERE session_id=? ORDER BY id ASC",
        (session_id,)
    )
    rows = cur.fetchall()
    db.close()
    return [{"user": r[0], "ai": r[1]} for r in rows]
