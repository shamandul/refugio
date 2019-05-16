#django.wsgi
import os, sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'refugio/refugio.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/webweave/tmp/trac-eggs/'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()