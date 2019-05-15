#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Add the project to the python path
import os, sys

sys.path.append('/home/webweave/refugio.webweaver.es/refugio/')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Prevent mod_wsgi from erroring on stdout access (WSGIRestrictStdout Off)
sys.stdout = sys.stderr

os.environ['PYTHON_EGG_CACHE'] = '/home/webweave/tmp/trac-eggs/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'refugio.settings'
import traceback
filename = '/home/usuarioquijost/public_html/error_log.txt'
f = open(filename, 'w')

try:
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()
    f.write('Ok')
except:
  traceback.print_exc(file=f)
f.close()


