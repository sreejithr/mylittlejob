# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from .core import SpotifySearchAPI


def home(request):
    return render(request, 'spotify_search/index.html')


class Search(View):
    spotify = SpotifySearchAPI()

    def get(self, request, *args, **kwargs):
        keyword = request.GET.get('q', None)
        filter_by = request.GET.get('filter_by', 'artist')

        if keyword:
         result = {
            'items': self.spotify.bsearch(keyword).filter_by(filter_by).execute(),
            'type': filter_by
        }

        return render(request, "spotify_search/index.html")
