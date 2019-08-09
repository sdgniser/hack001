"""
Coding Club's Hackathon
Date: 09 August 2019
Theme: Web APIs
"""

import requests
from bs4 import BeautifulSoup

import shutil

comic = requests.get('https://xkcd.com/456')
soup = BeautifulSoup(comic.text, 'html.parser')

comic_div = soup.select('div#comic > img')[0]
comic_url = 'https:' + comic_div['src']
comic_text = comic_div['title']

# Saving a PNG of the comic
with open('comic.png', 'wb') as f:
    comic_image = requests.get(comic_url, stream=True)
    comic_image.raw.decode_content = True
    shutil.copyfileobj(comic_image.raw, f)
    print(comic_text)
