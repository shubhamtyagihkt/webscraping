import urllib.request as ur, urllib.parse as up, urllib.error as ue
from bs4 import BeautifulSoup as bs
import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = r'http://py4e-data.dr-chuck.net/comments_918404.html'
html  = ur.urlopen(url, context=ctx).read()

soup = bs(html, 'html.parser')

spans = soup('span')
sum = 0
nums = [int(re.findall(r"> *([0-9]+) *</span>", str(span))[0]) for span in spans]

sum = 0
for e in nums:
    sum += e
print(sum)