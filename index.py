#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Add the project to the python path
import os, sys

sys.path.append('/home/webweave/refugio.webweaver.es/refugio/')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Prevent mod_wsgi from erroring on stdout access (WSGIRestrictStdout Off)
sys.stdout = sys.stderr

os.environ['PYTHON_EGG_CACHE'] = '/home/webweave/tmp/trac-eggs/'
os.environ['DJANGO_SETTINGS_MODULE'] = 'refugio.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

# Debug middleware
if settings.DEBUG:
    print >> sys.stderr, "Using Paste error middleware"
    from paste.exceptions.errormiddleware import ErrorMiddleware

    application = ErrorMiddleware(application, debug=True, show_exceptions_in_wsgi_errors=True)

# Create session directory if not present
if settings.SESSION_FILE_PATH:
    try:
        os.makedirs(settings.SESSION_FILE_PATH)
    except OSError:
        pass


def application(environ, start_response):
    import sys
    output = 'Python version: ' + str(sys.version) + '<br/>'

    import django
    output += 'Django version: ' + str(django.VERSION) + '<br/>'

    status = '200 OK'
    response_headers = [('Content-type', 'text/html;charset=UTF-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
