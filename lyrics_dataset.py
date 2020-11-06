import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("lyrics_translated.csv")
    df = df.dropna(subset=["lyrics"])
    lyric_str = " <|endoftext|> ".join(df['lyrics'].tolist())
    with open('lyrics.txt', 'w') as f:
        f.write(lyric_str)
