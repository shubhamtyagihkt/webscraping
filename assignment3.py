import xml.etree.ElementTree as ET
import urllib.request as ur, urllib.parse as up, urllib.error as ue

import ssl
import re

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = r'http://py4e-data.dr-chuck.net/comments_918406.xml'

plain_xml = ur.urlopen(url).read()

tree = ET.fromstring(plain_xml)

counts = tree.findall('.//count')

sum = 0

for count in counts:
    sum += int(count.text)

print(sum)