# -*- coding: utf-8 -*-
from .common import *  # noqa

DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('DJANGO_SECRET_KEY', default='-l8*-080ncm&+0-8szwl1z(j-o9d@e!zyl6xbfglu-okn*nv49')

EMAIL_PORT = 1025
EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

# django-debug-toolbar
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']

# INTERNAL_IPS = ['127.0.0.1', '10.0.2.2']

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
