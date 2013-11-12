DISPLAY_PAGES_ON_MENU = True

AUTHOR = u"Mohammad Tayseer"
SITENAME = u"Mohammad Tayseer"
#SITEURL = 'http://mtayseer.net'
SITEURL = '/'

TIMEZONE = 'Africa/Cairo'

DEFAULT_LANG = 'en'

MENUITEMS = [
    ("talks", "/talks/"),
    ("projects", "/projects/"),
    ("about", "/about/"),
]

VERSION = '5'
THEME = 'theme/arden'
CSS_FILE = "main.css?v=" + VERSION

DEFAULT_PAGINATION = False

DISQUS_SITENAME = 'mtayseer'

GOOGLE_ANALYTICS = 'UA-35924859-1'

TYPOGRIFY = True
DEFAULT_DATE_FORMAT = '%d %b %Y'

# To get pretty URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/'
ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}-{lang}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = False
TAG_URL = 'tags/{slug}/'
TAG_SAVE_AS = 'tags/{slug}/index.html'

# For cleaner output files
DELETE_OUTPUT_DIRECTORY = False

STATIC_PATHS = ['images', 'files']
