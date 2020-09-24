# install BeautifulSoup for this to work

import urllib.request as ur, urllib.parse as up, urllib.error as ue
from bs4 import BeautifulSoup as bs
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html  = ur.urlopen(url, context=ctx).read()

soup = bs(html, 'html.parser')

# retrive all anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
