from datetime import datetime

AUTHOR = 'st2d'
SITENAME = 'st2d'
SITEURL = 'https://st-2d.github.io/'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('過去の記事', '/archives.html'),
    ('カテゴリ', '/categories.html'),
    ('タグ', '/tags.html'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/st-2d'),
    ('twitter', 'https://x.com/cvtsuda')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Flex theme
DISABLE_URL_HASH = True
SITETITLE = 'st2d'
SITELOGO = '/image/favicon.png'
SITEDESCRIPTION = 'st2d webpage.'
OG_LOCALE = 'ja_JP'
COPYRIGHT_NAME = 'st2d'
COPYRIGHT_YEAR = f'2024 - {datetime.now().year}'
CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa',
}
FAVICON = '/image/favicon.png'
BROWSER_COLOR = 'orange'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
