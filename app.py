from database.setup import create_tables
from models.Song import Song
from models.Artist import Artist
from models.User import User
from models.Playlist import Playlist
from colorama import Fore, Style

def initialize():
    print("Creating tables...")
    create_tables()  
    print("Tables created successfully.")

def display_menu():
    print(Fore.GREEN + Style.BRIGHT + "===== Welcome to SongApp =====")
    print(Style.DIM + "\nAvailable Options:")
    print(Fore.RED + "1. Add Song")
    print("2. Add Artist")
    print("3. Add User")
    print("4. Create Playlist")
    print("5. Display Songs")
    print("6. Display Artists")
    print("7. Display Users")
    print("8. Display Playlists")
    print("9. Add Song to Playlist")
    print("10. Delete Song")
    print("11. Delete Artist")
    print("12. Delete User")
    print("13. Delete Playlist")
    print("14. Exit")
    print(Style.RESET_ALL)

def delete_song():
    song_id = input("Enter song ID to delete: ")
    Song.delete_song(song_id)

def delete_artist():
    artist_id = input("Enter artist ID to delete: ")
    Artist.delete_artist(artist_id)

def delete_user():
    user_id = input("Enter user ID to delete: ")
    User.delete_user(user_id)

def delete_playlist():
    playlist_id = input("Enter playlist ID to delete: ")
    Playlist.delete_playlist(playlist_id)

def add_song():
    title = input("Enter song title: ")
    artist_id = int(input("Enter artist ID: "))
    album_id = int(input("Enter album ID: "))
    release_date = input("Enter release date (YYYY-MM-DD): ")
    duration = input("Enter song duration (e.g., 3:45): ")
    Song(title, artist_id, album_id, release_date, duration)
    print("Song added successfully!")

def add_artist():
    name = input("Enter artist's name: ")
    Artist(name)
    print("Artist added successfully!")

def add_user():
    name = input("Enter user's name: ")
    email = input("Enter user's email: ")
    User(name, email)
    print("User added successfully!")

def create_playlist():
    name = input("Enter playlist name: ")
    user_id = int(input("Enter user ID: "))
    Playlist(name, user_id)
    print("Playlist created successfully!")

def add_song_to_playlist():
    playlist_id = int(input("Enter playlist ID: "))
    song_id = int(input("Enter song ID: "))
    playlist = Playlist(name="", user_id=0)
    playlist._id = playlist_id
    playlist.add_song(song_id)
    print("Song added to playlist successfully!")

def display_songs():
    songs = Song.get_all()  
    print("Songs:")
    for song in songs:
        print(f"ID: {song[0]}, Title: {song[1]}, Artist ID: {song[2]}, Album ID: {song[3]}, Release Date: {song[4]}, Duration: {song[5]}")

def display_artists():
    artists = Artist.get_all()
    print("Artists:")
    for artist in artists:
        print(f"ID: {artist[0]}, Name: {artist[1]}")

def display_users():
    users = User.get_all()
    print("Users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

def display_playlists():
    playlists = Playlist.get_all()
    print("Playlists:")
    for playlist in playlists:
        print(f"ID: {playlist[0]}, Name: {playlist[1]}, User ID: {playlist[2]}")

def main():
    initialize()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_song()
        elif choice == '2':
            add_artist()
        elif choice == '3':
            add_user()
        elif choice == '4':
            create_playlist()
        elif choice == '5':
            display_songs()
        elif choice == '6':
            display_artists()
        elif choice == '7':
            display_users()
        elif choice == '8':
            display_playlists()
        elif choice == '9':
            add_song_to_playlist()
        elif choice == '10':
            delete_song()
        elif choice == '11':
            delete_artist()
        elif choice == '12':
            delete_user()
        elif choice == '13':
            delete_playlist()
        elif choice == '14':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
