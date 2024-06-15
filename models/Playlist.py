from database.connection import get_db_connection

class Playlist:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id
        self._id = None

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO playlists (name, user_id)
            VALUES (?, ?)
        ''', (self._name, self._user_id))
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
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("User ID must be a positive integer")
        self._user_id = value

    def add_song(self, song_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO playlist_songs (playlist_id, song_id, added_at)
            VALUES (?, ?, ?)
        ''', (self.id, song_id, datetime.now().isoformat()))
        conn.commit()
        conn.close()

    def songs(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT songs.* FROM songs
            JOIN playlist_songs ON songs.song_id = playlist_songs.song_id
            WHERE playlist_songs.playlist_id = ?
        ''', (self.id,))
        songs = cursor.fetchall()
        conn.close()
        return songs

    def __repr__(self):
        return f"<Playlist(id={self.id}, name={self.name}, user_id={self.user_id})>"
    
    
    # 
