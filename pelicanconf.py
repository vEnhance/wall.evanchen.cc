from pathlib import Path

AUTHOR = "Evan Chen"
SITENAME = "talking to a wall"
SITEURL = ""
SITESUBTITLE = "because adulthood is too lonely for irl friends"

PATH = "content"

TIMEZONE = "US/Eastern"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme"
DEFAULT_PAGINATION = 5

TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""

OUTPUT_PATH = "/tmp/wall.evanchen.cc"
if not Path(OUTPUT_PATH).exists():
    Path(OUTPUT_PATH).mkdir()

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
