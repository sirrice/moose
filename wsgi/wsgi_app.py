#! /usr/bin/env python2.7
import sys
import os
import django.core.handlers.wsgi
sys.path.append('/home/django/')
sys.path.append('/data/django/moose/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'moose.settings'
application = django.core.handlers.wsgi.WSGIHandler()

