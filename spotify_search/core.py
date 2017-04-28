# -*- coding: utf-8 -*-

import requests

from abc import ABCMeta, abstractmethod


class MissingKeywordError(Exception):
    pass


class MissingFilterByError(Exception):
    pass


class BaseSpotifySearchAPI:
    __metaclass__ = ABCMeta

    @abstractmethod
    def search(self, keyword):
        pass
    
    @abstractmethod
    def filter_by(self, f):
        pass

    @abstractmethod
    def execute(self):
        pass


class SpotifySearchAPI(BaseSpotifySearchAPI):
    url = "https://api.spotify.com/v1/search"
    keyword = None
    filters = {}

    def _clean_keyword(self, keyword):
        w = keyword.replace('"', '')
        return w.replace(' ', '+')

    def search(self, keyword):
        if keyword:
            self.keyword = self._clean_keyword(keyword)
        return self

    def filter_by(self, f):
        """
        Possible values for f are:
        1. artist
        2. album
        3. playlist
        4. track

        """
        if f:
            self.filters['type'] = f
        return self

    def execute(self):
        if not self.keyword:
            raise MissingKeywordError

        if 'type' not in self.filters:
            raise MissingFilterByError

        params = {'q': self.keyword}
        for key, value in self.filters.items():
            params[key] = value

        r = requests.get(self.url, params=params)

        if r.status_code == 200:
            if self.filters.get('type', None) == 'artist':
                return r.json().get('artists', None)
            elif self.filters.get('type', None) == 'album':
                return r.json().get('album', None)
            elif self.filters.get('type', None) == 'playlist':
                return r.json().get('playlists', None)
            elif self.filters.get('type', None) == 'track':
                return r.json().get('track', None)

        return []
