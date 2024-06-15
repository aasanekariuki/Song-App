import sqlite3

def get_db_connection():
    return sqlite3.connect('songs.db')

class Song:
    def __init__(self, title, artist_id, album_id, release_date, duration):
        self._title = title
        self._artist_id = artist_id
        self._album_id = album_id
        self._release_date = release_date
        self._duration = duration
        self._id = None

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO songs (title, artist_id, album_id, release_date, duration)
            VALUES (?, ?, ?, ?, ?)
        ''', (self._title, self._artist_id, self._album_id, self._release_date, self._duration))
        self._id = cursor.lastrowid
        conn.commit()
        conn.close()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def artist_id(self):
        return self._artist_id

    @artist_id.setter
    def artist_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Artist ID must be a positive integer")
        self._artist_id = value

    @property
    def album_id(self):
        return self._album_id

    @album_id.setter
    def album_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Album ID must be a positive integer")
        self._album_id = value

    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Release date must be a non-empty string")
        self._release_date = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Duration must be a non-empty string")
        self._duration = value

    def artist(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM artists WHERE artist_id = ?', (self.artist_id,))
        artist = cursor.fetchone()
        conn.close()
        return artist

    def album(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM albums WHERE album_id = ?', (self.album_id,))
        album = cursor.fetchone()
        conn.close()
        return album

    def __repr__(self):
        return f"<Song(id={self.id}, title={self.title}, artist_id={self.artist_id}, album_id={self.album_id}, release_date={self.release_date}, duration={self.duration})>"

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM songs')
        songs = cursor.fetchall()
        conn.close()
        return songs

    @staticmethod
    def delete_song(song_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM songs WHERE song_id = ?', (song_id,))
        conn.commit()
        conn.close()
