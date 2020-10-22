import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config import PLAYLIST_ID
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.user_playlist_tracks("spijekrvet", PLAYLIST_ID)

tracks = results['items']
while results['next']:
    results = spotify.next(results)
    tracks.extend(results['items'])

for t in tracks:
    print(t["track"].keys())
    break