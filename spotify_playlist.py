import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    token = spotipy.util.prompt_for_user_token("spijkervet", "playlist-modify-public")
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    df = pd.read_csv("dataset.csv")
    ids = []
    for idx, row in df.iterrows():
        artist = row["artist"]
        song_title= row["song"]

        s = spotify.search(q=f"{song_title} {artist}", type="track")
        tracks = s["tracks"]["items"]
        if len(tracks):
            first_track = tracks[0]
            spotify_uri = first_track["uri"]
            # print("Found {} {} {}".format(artist, song_title, spotify_uri))
            ids.append(spotify_uri)
        else:
            print("Did not find {} {} on Spotify".format(artist, song_title))

    token = spotipy.util.prompt_for_user_token("spijkervet", "playlist-modify-public")
    spotify = spotipy.Spotify(auth=token)
    playlist_id = "5Gm8xejfbZln7cfc1jvh5T"
    for i in chunks(ids, 100):
        print("Added {} items to playlist {}".format(len(i), playlist_id))
        spotify.playlist_add_items(playlist_id, i)

    print("Found {} of {} tracks on Spotify".format(len(ids), len(df)))