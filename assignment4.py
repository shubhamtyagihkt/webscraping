import json
import urllib.request as ur, urllib.parse as up, urllib.error as ue

import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = r'http://py4e-data.dr-chuck.net/comments_918407.json'

plain_json = ur.urlopen(url).read().decode()

js = json.loads(plain_json)

sum = 0

for count in js["comments"]:
    sum += int(count["count"])

print(sum)