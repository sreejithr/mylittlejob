# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import home, search

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/(?P<keyword>[a-zA-Z0-9+]+)', search, name='search'),
    url(r'^search/', search, name='ajax_search')
]
