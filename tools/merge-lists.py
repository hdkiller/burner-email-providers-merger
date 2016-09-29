#!/bin/python
##
from pprint import pprint
from urllib.request import urlopen
import os

sources = []
emails = []

# download and merge domains from urls found in sources directory

files = []
for (path, dirnames, filenames) in os.walk('../sources'):
    files.extend(os.path.join(path, name) for name in filenames)

for fname in files:
    with open(fname) as infile:
        for line in infile:
            if line not in sources:
                sources.append(line.strip())

# download urls found in files
for source in sources:
    response = urlopen(source.strip())
    html = response.read()
    for domain in html.split():
        email = domain.decode("utf-8").strip()
        if email not in emails:
            emails.append(email)

# merge files in lists directory

files = []
for (path, dirnames, filenames) in os.walk('../lists'):
    files.extend(os.path.join(path, name) for name in filenames)


for fname in files:
    with open(fname) as infile:
        for line in infile:
            if line.strip() not in emails:
                emails.append(line.strip())

emails.sort()
with open('../emails.txt', 'w') as f:
    f.write("\n".join(emails))
