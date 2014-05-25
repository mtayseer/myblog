DISPLAY_PAGES_ON_MENU = True

AUTHOR = u"Mohammad Tayseer"
SITENAME = u"Mohammad Tayseer"
#SITEURL = 'http://mtayseer.net'
SITEURL = '/'

PATH = 'content'

TIMEZONE = 'Africa/Cairo'

DEFAULT_LANG = 'en'

MENUITEMS = [
    ("Talks", "/tags/talks/"),
    ("Projects", "/projects/"),
    ("About", "/about/"),
]

VERSION = '8'
THEME = 'theme/littlebigdetails'
CSS_FILE = "main.css?v=" + VERSION

DEFAULT_PAGINATION = 10

DISQUS_SITENAME = 'mtayseer'

GOOGLE_ANALYTICS = 'UA-35924859-1'

TYPOGRIFY = False
DEFAULT_DATE_FORMAT = '%d %b %Y'

# To get pretty URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

# For cleaner output files
DELETE_OUTPUT_DIRECTORY = False

STATIC_PATHS = ['images', 'files']

SOCIAL_LINKS = [
    ('Twitter',  'http://twitter.com/m_tayseer'),
    ('Facebook', 'http://facebook.com/mohammad.tayseer'),
    ('Github',   'http://github.com/mtayseer'),
    ('Email',    'mailto:mtayseer82 -at- gmail.com'),
]

