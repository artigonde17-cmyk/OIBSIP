import sqlite3

# Create database connection
conn = sqlite3.connect("chats.db")

cursor = conn.cursor()

# Create messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    username TEXT,
    message TEXT
)
""")

conn.commit()

# Save messages
def save_message(username, message):

    cursor.execute(
        "INSERT INTO messages VALUES (?, ?)",
        (username, message)
    )

    conn.commit()

# Fetch all messages
def get_messages():

    cursor.execute("SELECT * FROM messages")

    return cursor.fetchall()