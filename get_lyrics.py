import os
import pandas as pd
import numpy as np
import lyricsgenius

from dotenv import load_dotenv

def get_lyrics(row):
    lyrics = ""

    if not pd.isnull(row["song"]):
        artist = genius.search_artist(row["artist"], max_songs=0)
        songs = genius.search_songs(search_term="{} {}".format(row["song"], artist.name))
        if songs:
            if len(songs["hits"]):
                lyrics_path = songs["hits"][0]["result"]["path"]
                lyrics = genius.lyrics("https://genius.com" + lyrics_path)
        
    row["lyrics"] = lyrics
    return row

if __name__ == "__main__":
    load_dotenv()
    genius_access_token = os.getenv('GENIUS_ACCESS_TOKEN')
    genius = lyricsgenius.Genius(genius_access_token)

    df = pd.read_csv("dataset.csv")   
    df = df.apply(get_lyrics, axis=1)
    df.to_csv("lyrics.csv", index=False)