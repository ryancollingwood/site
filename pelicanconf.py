#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Collingwood'
SITENAME = 'ryancollingwood.info'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Blog', '/index.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
    )

# Social widget
SOCIAL = (
    ('linkedin', 'https://linkedin.com/in/ryancollingwood'),
    ('github', 'https://github.com/ryancollingwood'),
    ('rss', '//feeds/all.atom.xml'),
    )

DEFAULT_PAGINATION = 10

STATIC_PATHS = [
    'images',
    'favicon.ico',
    ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
TYPOGRIFY = True
THEME = 'Flex'