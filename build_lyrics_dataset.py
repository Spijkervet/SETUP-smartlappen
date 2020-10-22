import re
import pandas as pd
from sklearn.model_selection import train_test_split


def build_text_files(df, dest_path):
    with open(dest_path, "w") as f:
        data = ''
        for _, row in df.iterrows():
            summary = str(row["lyrics"]).strip()
            summary = re.sub(r"\s", " ", summary)
            data += summary + "  "
        f.write(data)

if __name__ == "__main__":
    df = pd.read_csv("lyrics.csv")

    train, test = train_test_split(df, test_size=0.2)

    build_text_files(train, 'train_dataset.txt')
    build_text_files(test, 'test_dataset.txt')

    print("Train dataset length: " + str(len(train)))
    print("Test dataset length: " + str(len(test)))