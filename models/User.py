import sqlite3

def get_db_connection():
    return sqlite3.connect('songs.db')

class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email
        self._id = None
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (name, email)
            VALUES (?, ?)
        ''', (self._name, self._email))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Email must be a non-empty string")
        self._email = value

    def playlists(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM playlists WHERE user_id = ?', (self.id,))
        playlists = cursor.fetchall()
        conn.close()
        return playlists

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        conn.close()
        return users

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        conn.commit()
        conn.close()
        
        
# 
