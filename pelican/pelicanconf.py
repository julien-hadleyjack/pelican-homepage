#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Hadley Jack'
SITENAME = 'Julien Hadley Jack'
SITESUBTITLE = ''
SITEURL = 'hadleyjack.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'Uncategorized'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('google-plus-sign', 'https://plus.google.com/+JulienHadleyJack'),
          ('github', 'https://github.com/julien-hadleyjack/'),)

DEFAULT_PAGINATION = 10

THEME = "./themes/pelican-cait"

#TYPOGRIFY(True)

DISPLAY_PAGES_ON_MENU = True

# USE_CUSTOM_MENU = True
# CUSTOM_MENUITEMS = (('Blog', 'blog'),
#                     ('Contact', 'contact-me'),
#                     ('Projects', 'pages/projects'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
