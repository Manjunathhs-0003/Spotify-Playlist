from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv()


SPOTIFY_APP_CLIENT = os.getenv("SPOTIFY_APP_CLIENT")
SPOTIFY_APP_CLIENT_SECRET = os.getenv("SPOTIFY_APP_CLIENT_SECRET")
SPOTIFY_REDIRECT_URL = os.getenv("SPOTIFY_REDIRECT_URL")

def scrape_billboard_and_create_playlist():
    # Scraping Billboard 100
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
    soup = BeautifulSoup(response.text, 'html.parser')
    song_names_spans = soup.select("li ul li h3")
    song_names = [song.getText().strip() for song in song_names_spans]

    # Spotify Authentication
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth
                         (client_id=SPOTIFY_APP_CLIENT,
                          client_secret=SPOTIFY_APP_CLIENT_SECRET,
                          redirect_uri=SPOTIFY_REDIRECT_URL,
                          show_dialog=True,
                          cache_path="token.txt",
                          username="ManjunathHS0003",
                          scope="playlist-modify-private playlist-read-private"))

    user_id = sp.current_user()["id"]

    # Searching Spotify for songs by title
    song_uris = []
    year = date.split("-")[0]
    for song in song_names:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")

    # Prompt the user for the playlist name
    playlist_name = input("Enter the custom name for the playlist: ")

    # Creating a new private playlist in Spotify with the custom name
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)

    # Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

    print("Playlist created successfully!")

if __name__ == "__main__":
    scrape_billboard_and_create_playlist()
