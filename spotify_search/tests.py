# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from test_plus.test import TestCase

from core import SpotifySearchAPI


class SearchTest(TestCase):
    spotify = SpotifySearchAPI()

    def get_result(self, keyword, filter_by):
        return self.spotify.search(keyword).filter_by(filter_by).execute()

    def test_if_search_returns_proper_count(self):
        # Filter by artist
        keyword, filter_by = "led+zeppelin", "artist"
        result = self.get_result(keyword, filter_by)

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertEqual(
            result and result.get('total'),
            r.context.get('count')
        )

        # Filter by album
        keyword, filter_by = "led+zeppelin", "album"
        result = self.get_result(keyword, filter_by)

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertEqual(
            result and result.get('total'),
            r.context.get('count')
        )

        # Filter by playlist
        keyword, filter_by = "led+zeppelin", "playlist"
        result = self.get_result(keyword, filter_by)

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertEqual(
            result and result.get('total'),
            r.context.get('count')
        )

        # Filter by track
        keyword, filter_by = "led+zeppelin", "track"
        result = self.get_result(keyword, filter_by)

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertEqual(
            result and result.get('total'),
            r.context.get('count')
        )

    def test_if_search_returns_all_results(self):
        # Filter by album
        keyword, filter_by = "led+zeppelin", "album"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by artist
        keyword, filter_by = "led+zeppelin", "artist"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by playlist
        keyword, filter_by = "led+zeppelin", "playlist"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by track
        keyword, filter_by = "led+zeppelin", "track"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("search", keyword=keyword) + "?filter_by=" + filter_by
        r = self.client.get(url)

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

    def test_if_ajax_search_returns_all_results(self):
        # Filter by artist
        keyword, filter_by = "led+zeppelin", "album"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("ajax_search")
        r = self.client.post(url, {
            'q': keyword,
            'filter_by': filter_by,
        })

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by artist
        keyword, filter_by = "led+zeppelin", "playlist"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("ajax_search")
        r = self.client.post(url, {
            'q': keyword,
            'filter_by': filter_by,
        })

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by artist
        keyword, filter_by = "led+zeppelin", "artist"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("ajax_search")
        r = self.client.post(url, {
            'q': keyword,
            'filter_by': filter_by,
        })

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

        # Filter by artist
        keyword, filter_by = "led+zeppelin", "track"
        result = self.get_result(keyword, filter_by)

        name_first_result = result['items'][0]['name']
        name_last_result = result['items'][-1]['name']

        url = self.reverse("ajax_search")
        r = self.client.post(url, {
            'q': keyword,
            'filter_by': filter_by,
        })

        self.assertContains(r, name_first_result)
        self.assertContains(r, name_last_result)

