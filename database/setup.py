import sqlite3

def create_tables():
    conn = sqlite3.connect('songs.db')
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS artists (
        artist_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS albums (
        album_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        release_date TEXT
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS songs (
        song_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        artist_id INTEGER,
        album_id INTEGER,
        release_date TEXT,
        duration TEXT,
        FOREIGN KEY(artist_id) REFERENCES artists(artist_id),
        FOREIGN KEY(album_id) REFERENCES albums(album_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS playlists (
        playlist_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    ''')

    c.execute('''
    CREATE TABLE IF NOT EXISTS playlist_songs (
        playlist_id INTEGER,
        song_id INTEGER,
        added_at TEXT,
        PRIMARY KEY (playlist_id, song_id),
        FOREIGN KEY(playlist_id) REFERENCES playlists(playlist_id),
        FOREIGN KEY(song_id) REFERENCES songs(song_id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__': 
    create_tables()
