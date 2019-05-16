#django.wsgi
import os, sys
sys.path.append('/home/webweave/refugio.webweaver.es/refugio/modules')
sys.path.append('/home/webweave/refugio.webweaver.es/refugio/modules/django')
sys.path.append('/home/webweave/refugio.webweaver.es/refugio')
os.environ['DJANGO_SETTINGS_MODULE'] = 'refugio/refugio.settings'
os.environ['PYTHON_EGG_CACHE'] = '/home/webweave/tmp/trac-eggs/'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()