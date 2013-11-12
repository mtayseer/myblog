import requests, urlparse, sys
from lxml.html import fromstring

all_links = set()
visited = set()
deadlinks = set()

#url = 'http://mtayseer.net/'
url = 'http://localhost:8000/'
all_links.add(url)

while all_links:
    link = all_links.pop()
    visited.add(link)
    try:
        r = requests.get(link)
    except:
        print link
    else:
        if not r.ok:
            deadlinks.add(link)
            continue

        if url not in link:
            continue

        doc = fromstring(r.content)
        for elt in doc.cssselect('a'):
            href = urlparse.urljoin(url, elt.get('href', ''))
            if href not in visited:
                all_links.add(href)

print 'Found {0} dead links in {1} links'.format(len(deadlinks), len(visited))
open('dead_links.txt', 'w').write('\n'.join(deadlinks))