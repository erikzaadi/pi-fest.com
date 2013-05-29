#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'erikzaadi'
SITENAME = u'Pi-Fest.com'
#SITEURL = 'http://pi-fest.com'

TIMEZONE = 'Asia/Jerusalem'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Raspberry Pi', 'http://www.raspberrypi.org/'))

THEME = 'deps/pelican-cait'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    ('Contact', 'contact.html'),
    ('Events', 'category/events.html'),
    ('Blog', 'category/blog.html'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
GITHUB_URL = "http://github.com/erikzaadi/pi-fest.com"

PLUGIN_PATH = 'deps/pelican-plugins'
PLUGINS = ['assets', 'sitemap']

STATIC_PATHS = ['images', 'js', 'css']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
TYPOGRIFY = True

FILES_TO_COPY = (
    ('extra/robots.txt', 'robots.txt'),
    ('extra/favicon.ico', 'favicon.ico'),
    ('extra/favicon.png', 'favicon.png'),
    ('extra/humans.txt', 'humans.txt'),)
