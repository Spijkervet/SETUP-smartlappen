# SETUP x Smartlappen
SETUP x Smartlappen project

## Requirements
```
Python 3.5+
tensorflow
scrapy
```

## Data
Pre-training is done on the LAKH MIDI dataset, which can be downloaded here: https://colinraffel.com/projects/lmd/
Fine-tuning is done on MIDI files located in the `data` sub-folder.

Extracting piano parts can be done with:
```
python extract_piano_order.py
```

## Lyrics
The `songtekstsen.nl` lyrics scraper is located in the `songteksten` folder. You can run the scraper with:
```
pip3 install scrapy
cd songteksten
scrapy crawl songs
```



## Logic Pro X Project
The write session project file is located in `write sessionlogicx`, and can be opened using Logic Pro X 10+

## Ideas
AI ideas are generated during the writing sessions located in the `smartlap` folder.
The `bounces` folder contains printed stems of these ideas used in the SETUP podcast.
