import pandas as pd
from googletrans import  Translator
from tqdm import tqdm
import time
# from langdetect import detect

# def translate(row):
#     if not pd.isnull(row["lyrics"]):
#         # lang = detect(row["lyrics"])
#         if "nigga" in row["lyrics"].lower() or "fuck" in row["lyrics"].lower() or "neuken" in row["lyrics"].lower() or "money" in row["lyrics"].lower():
#             row["lyrics"] = ""
#         else:
#             row["lyrics"] = translator.translate(row["lyrics"], dest='en').text
#     return row

if __name__ == "__main__":
    df = pd.read_csv("./lyrics_dataset.csv")
    translator = Translator()
    # df = df.apply(translate, axis=1)

    with open("lyrics_translated.txt", "w") as f:
        for _, row in tqdm(df.iterrows(), total=len(df)):

            if type(row["lyrics"]) == str:
                if "nigga" in row["lyrics"].lower() or "fuck" in row["lyrics"].lower() or "neuken" in row["lyrics"].lower() or "money" in row["lyrics"].lower():
                    continue

                lyrics = row["lyrics"]

                try:
                    # for l in lyrics.split("\n"):
                    lyrics_nl = translator.translate(lyrics, dest='en').text
                    if lyrics_nl != lyrics:
                        f.write(lyrics_nl)
                        f.write(" <|endoftext|> ")
                        f.write("\n")
                except Exception as e:
                    print("Failed {}".format(row["song"]))
                    print(e)
                    time.sleep(20)

