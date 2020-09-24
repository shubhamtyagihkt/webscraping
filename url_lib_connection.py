# Since HTTP is so common, we have a library that does all the socket work for us and makes
# web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://example.com')
for line in fhand:
    print(line.decode().strip())