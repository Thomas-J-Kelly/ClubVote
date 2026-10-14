import sqlite3
from club import Member

DATABASE_NAME = 'club.db'

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

connection = get_connection()
cursor = connection.cursor()


def create_tables():
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS members
        (id INTEGER PRIMARY KEY,
            name TEXT NOT NULL)
        """
    )
    connection.commit()
    connection.close()


def add_member(member):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO members (name) VALUES (?)",
        (member.name,)
    )
    member.ID = cursor.lastrowid
    connection.commit()
    connection.close()
    
def get_member(member_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT id, name FROM members WHERE id = ?",
        (member_id,)
    )
    row = cursor.fetchone()
    connection.close()
    if row:
        return Member(row[1], row[0])
    return None

