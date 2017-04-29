# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.template.loader import render_to_string

from .core import SpotifySearchAPI


def home(request):
    return render(request, 'spotify_search/index.html', context={'type': 'artist'})


def search(request, *args, **kwargs):
    spotify = SpotifySearchAPI()

    if (request.method == 'POST'):
        keyword = request.POST.get('q', None)
        filter_by = request.POST.get('filter_by', 'artist')

        if keyword:
            result = spotify.search(keyword).filter_by(filter_by).execute()

            if not result:
                return JsonResponse({})

            resultList = render_to_string(
                'spotify_search/results.html', {
                    'items': result.get('items', []),
                    'type': filter_by,
                }
            )

            data = {
                'resultList': resultList,
                'type': filter_by,
                'count': result.get('total', 0),
            }
        else:
            data = {
                'resultList': [],
                'type': filter_by,
                'count': 0,
            }

        return JsonResponse(data)

    else:
        keyword = kwargs.get('keyword', None)
        filter_by = request.GET.get('filter_by', 'artist')

        if keyword:
            result = spotify.search(keyword).filter_by(filter_by).execute()

            if not result:
                return render(request, "spotify_search/index.html", context={
                    'items': None,
                    'type': filter_by,
                    'count': None,
                    'q': keyword,
                })

            context = {
                'items': result.get('items', None),
                'type': filter_by,
                'count': result.get('total', None),
                'q': keyword,
            }
        else:
            context = {
                'items': None,
                'type': filter_by,
                'count': None,
                'error_msg': 'Please supply the search term',
            }

        return render(request, "spotify_search/index.html", context=context)

