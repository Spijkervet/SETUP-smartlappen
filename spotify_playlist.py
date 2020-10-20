import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())



if __name__ == "__main__":
    df = pd.read_csv("dataset.csv")
    ids = []
    for idx, row in df.iterrows():
        artist = row["artist"]
        song_title= row["song"]

        s = spotify.search(q="artist:{} track:{}".format(artist, song_title), type="track")
        tracks = s["tracks"]["items"]
        if len(tracks):
            first_track = tracks[0]
            spotify_uri = first_track["uri"]
            # print("Found {} {} {}".format(artist, song_title, spotify_uri))
            ids.append(spotify_uri)
        else:
            print("Did not find {} {} on Spotify".format(artist, song_title))

    with open("spotify_ids.txt", "w") as f:
        for i in ids:
            f.write("{}\n".format(i))

    print("Found {} of {} tracks on Spotify".format(len(ids), len(df)))