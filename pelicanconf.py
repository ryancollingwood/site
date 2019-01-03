#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Collingwood'
SITENAME = 'ryancollingwood.info'
SITEURL = 'http://ryancollingwood.info/'

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
    ('Blog', '/index.html'),
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
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
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
TYPOGRIFY = True

MARKDOWN = {
  'extension_configs': {
    'pyembed.markdown': {}
  }
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ["plantuml"]

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
## google analytics (fake code commented out)
# GOOGLE_ANALYTICS = 'UA-0011001-1'
## Twitter username for Twitter Card data
TWITTER_USERNAME = '@ryancollingwood'
## Toggle display of theme attribution in the footer (scroll down and see)
## Attribution is appreciated but totally fine to turn off!
ATTRIBUTION = True
## Add a link to the tags page to the menu
## Other links can be added following the same tuple pattern 
MENUITEMS = [
    ('Profile', '/pages/profile.html'),
    ('Blog', '/index.html')
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
DISQUS_SITENAME = ''

## Gravatar
## Commenting mine out so you can see how the theme looks without one
GRAVATAR = 'https://www.gravatar.com/avatar/ea97dc5b577a9ea291c33cbf23cb8a32?s=256'
