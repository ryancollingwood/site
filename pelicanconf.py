#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Collingwood'
SITENAME = 'ryancollingwood.info'
SITEURL = ''
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', '/'),
    ('Archives', '/archives'),
    ('Categories', '/categories'),
    ('Tags', '/tags'),
    )

# Social widget
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/ryancollingwood'),
    ('github', 'https://github.com/ryancollingwood'),
    ('rss', 'feeds/all.atom.xml'),
    )

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images',
    'favicon.ico',
    ]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
TYPOGRIFY = True

MARKDOWN = {
  'extension_configs': {
    'pyembed.markdown': {},
    'markdown.extensions.codehilite': {
        'css_class': 'highlight',
        'linenums': False,
        'use_pygments': True
        },
    'markdown.extensions.extra': {},
    'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    "plantuml",
    "better_codeblock_line_numbering",
    ]

# Theme Settings
THEME = 'brutalist'
## used for OG tags and Twitter Card data on index page
SITEIMAGE = 'site-cover.jpg'
## used for OG tags and Twitter Card data of index page
SITEDESCRIPTION = 'Thoughts and musings by Ryan Collingwood'
## path to favicon
FAVICON = 'favicon.ico'
## path to logo for nav menu (optional)
LOGO = 'avatar.jpg'
## first name for nav menu if logo isn't provided
FIRST_NAME = 'Ryan'
## google analytics
GOOGLE_ANALYTICS = 'UA-131681263-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@ryancollingwood'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = False
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [
    ('Profile', '/profile'),
    ('Blog', '/')
    ]
## Social icons for footer
LINKEDIN = 'https://linkedin.com/in/ryancollingwood'
STRAVA = ''
TWITTER = 'https://twitter.com/ryancollingwood'
INSTAGRAM = ''
GITHUB = 'https://github.com/ryancollingwood'
TELEGRAM = ''
GOODREADS = ''
FOURSQUARE = ''
UNTAPPD = ''
## Disqus Sitename for comments on posts
## Commenting mine out for this theme site
DISQUS_SITENAME = 'ryancollingwood'

## Gravatar
## Commenting mine out so you can see how the theme looks without one
GRAVATAR = 'https://www.gravatar.com/avatar/ea97dc5b577a9ea291c33cbf23cb8a32?s=256'


ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = '{category}/{slug}-{lang}'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL
DRAFT_URL = 'drafts/{slug}'
DRAFT_PAGE_URL = 'drafts/{slug}'
DRAFT_PAGE_SAVE_AS = DRAFT_PAGE_URL
DRAFT_PAGE_LANG_URL = 'drafts/pages/{slug}-{lang}'
DRAFT_PAGE_LANG_SAVE_AS = DRAFT_PAGE_LANG_URL
DRAFT_SAVE_AS = DRAFT_URL
DRAFT_LANG_SAVE_AS = 'drafts/{slug}-{lang}'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL
PAGE_LANG_URL = 'pages/{slug}-{lang}'
PAGE_LANG_SAVE_AS = 'pages/{slug}-{lang}'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = CATEGORY_URL
CATEGORIES_SAVE_AS  = 'categories'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL
TAGS_SAVE_AS = 'tags'
AUTHOR_URL = 'author'
AUTHOR_SAVE_AS = AUTHOR_URL
AUTHORS_SAVE_AS = 'authors'
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_URL = ''
DAY_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_URL = ''
ARCHIVES_SAVE_AS = 'archives'
YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
DAY_ARCHIVE_SAVE_AS = ''
INDEX_SAVE_AS = 'index.html'




