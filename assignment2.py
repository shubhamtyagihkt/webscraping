import urllib.request as ur, urllib.parse as up, urllib.error as ue
from bs4 import BeautifulSoup as bs
import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = r'http://py4e-data.dr-chuck.net/known_by_Connolly.html'
count = 7
position = 18

while count >= 1:
    html  = ur.urlopen(url, context=ctx).read()
    soup = bs(html, 'html.parser')
    anc = soup('a')
    url = anc[position-1].get('href', None)
    if count == 1:
        print(re.findall(r"> *(.+) *</a>", str(anc[position-1]))[0])
    count -= 1
