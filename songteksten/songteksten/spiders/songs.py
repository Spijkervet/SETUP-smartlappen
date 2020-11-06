import scrapy
import html2text
from scrapy import Request
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

class SongsSpider(scrapy.Spider):
    name = 'songs'
    allowed_domains = ['songteksten.nl']
    start_urls = ['https://www.songteksten.nl/artiest/287/andre-hazes.htm']
    
    def start_requests(self):
        self.df = pd.DataFrame(columns=["artist", "song", "lyrics"])
        for u in self.start_urls:
            print(u)
            yield scrapy.Request(u, callback=self.parse)

    def parse(self, response):
        items = response.selector.xpath("//table//tr")

        artist = os.path.basename(response.url).replace(".htm", "")
        artist = artist.replace("-", " ")
        artist = artist.title()

        self.artist_file = open("{}_lyrics.txt".format(artist), "w")        

        for i in items:
            link = i.xpath(".//a/@href").get()
            song = i.xpath(".//a/span/text()").get().strip()
            print("Scraping {} - {}".format(artist, song))
            yield Request(url="http://songteksten.nl" + link, callback=self.parse_song, meta={"song": song, "artist": artist})

        self.artist_file.close()
    
    def parse_song(self, response):
        lyrics = response.selector.xpath(".//span[@itemprop='description']").get()

        soup = BeautifulSoup(lyrics, features="lxml")
        for div in soup.findAll('div'):
            div.extract()

        lyrics = re.sub("<.*?>", " ", soup.get_text())
        lyrics = lyrics.strip()

        artist = response.meta["artist"]
        song = response.meta["song"]
        

        self.df = self.df.append({"artist": artist, "song": song, "lyrics": lyrics}, ignore_index=True)
        self.df.to_csv("lyrics_dataset.csv", index=False)

        self.artist_file.write(lyrics)