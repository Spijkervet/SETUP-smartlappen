import pandas as pd
from googletrans import  Translator
from langdetect import detect

def translate(row):
    if not pd.isnull(row["lyrics"]):
        if detect(row["lyrics"]) == "nl":
            row["lyrics"] = translator.translate(row["lyrics"], dest='en').text
    return row

if __name__ == "__main__":
    df = pd.read_csv("./lyrics.csv")
    translator = Translator()
    df = df.apply(translate, axis=1)
    df.to_csv("lyrics_translated.csv", index=False)