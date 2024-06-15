import sqlite3

def get_db_connection():
    return sqlite3.connect('songs.db')

class Artist:
    def __init__(self, name):
        self._name = name
        self._id = None

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO artists (name) VALUES (?)', (self._name,))
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

    def songs(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM songs WHERE artist_id = ?', (self.id,))
        songs = cursor.fetchall()
        conn.close()
        return songs

    def __repr__(self):
        return f"<Artist(id={self.id}, name={self.name})>"

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM artists')
        artists = cursor.fetchall()
        conn.close()
        return artists

    @staticmethod
    def delete_artist(artist_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM artists WHERE artist_id = ?', (artist_id,))
        conn.commit()
        conn.close()
