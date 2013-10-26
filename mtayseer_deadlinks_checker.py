import requests, urlparse, sys
from lxml.html import fromstring

all_links = set()
visited = set()
deadlinks = set()

url = 'http://mtayseer.net/'
all_links.add(url)

while all_links:
    link = all_links.pop()
    print link in visited, link
    visited.add(link)
    r = requests.get(link)

    if not r.ok:
        deadlinks.add(link)
        continue

    if 'mtayseer.net' not in link:
        continue

    doc = fromstring(r.content)
    for elt in doc.cssselect('a'):
        href = urlparse.urljoin(url, elt.get('href', ''))
        if href not in visited:
            all_links.add(href)

print 'Found {0} dead links in {1} links'.format(len(deadlinks), len(visited))
open('dead_links.txt', 'w').write('\n'.join(deadlinks))