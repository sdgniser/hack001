"""
Coding Club's Hackathon
Date: 09 August 2019
Theme: Web APIs
"""

from pprint import pprint

import requests
from bs4 import BeautifulSoup

import shutil

potd_arg = {
    'api_key': 'DEMO_KEY'
}

potd_res = requests.get('https://api.nasa.gov/planetary/apod', params=potd_arg)
potd = potd_res.json()

# Saving the image in a PNG file
with open('image.png', 'wb') as f:
    image = requests.get(potd['url'], stream=True)
    image.raw.decode_content = True
    shutil.copyfileobj(image.raw, f)
