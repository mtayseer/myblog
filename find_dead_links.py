# Search my blog for dead web links, so I can keep them updated
import requests
from urlparse import urljoin
from lxml.html import fromstring

BASE_URL = 'http://localhost:7000/'

# A dictionary of all the links in the blog. The value 'True' means that the link is live, and 'False' means dead.
live_links, dead_links = set(), set()
links_q = set([BASE_URL])

def main():
    while links_q:
        print '{0} links in queue'.format(len(links_q))
        link = links_q.pop()
        req = requests.get(link)
        if not req.ok:
            dead_links.add(urljoin(BASE_URL, link))
        else:
            live_links.add(link)

            # Extract links from pages in our site only, not external sites
            if link.startswith(BASE_URL):
                d = fromstring(req.content)
                for l in d.cssselect('a'):
                    # If link already visited, ignore it
                    if l not in dead_links and l not in live_links and l not in links_q:
                        links_q.add(urljoin(BASE_URL, l.attrib['href']))

    with open('dead_links.txt', 'w') as out_file:
        out_file.write('\n'.join(dead_links))

    print '''
{0} dead links.
{1} live links
'''.format(len(dead_links), len(live_links))

if __name__ == '__main__':
    main()

