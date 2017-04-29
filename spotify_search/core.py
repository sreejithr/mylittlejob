# -*- coding: utf-8 -*-
import requests


class MissingKeywordError(Exception):
    pass


class MissingFilterByError(Exception):
    pass


class SpotifySearchAPI:
    url = "https://api.spotify.com/v1/search"
    keyword = None
    filters = {}

    def _clean_keyword(self, keyword):
        w = keyword.replace('"', '')
        return w.replace(' ', '+')

    def _add_thumbnails(self, results, result_type):
        def _add_thumbnail(result):
            """
            Adds a `thumbnail` key. Since the image dimensions in the
            result aren't uniform, we select one which is atleast 150 x 150
            and closest in dimensions to it.
            """
            if result_type == 'artist':
                images = result['images']

            elif result_type == 'album':
                images = result['images']

            elif result_type == 'playlist':
                images = result['images']

            elif result_type == 'track':
                images = result['album']['images']

            try:
                thumbnail = images[0]
            except IndexError:
                # No images in the result. We let the frontend code handle this.
                result['thumbnail'] = None
                return result

            for image in images:
                if image['width'] < 150 or image['height'] < 150:
                    continue

                if image['width'] - 150 + image['height'] - 150 <\
                   thumbnail['width'] - 150 + thumbnail['height'] - 150:
                    thumbnail = image

            result['thumbnail'] = thumbnail
            return result

        if results:
            results['items'] = map(
                lambda result: _add_thumbnail(result),
                results.get('items', []),
            )
            return results

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
                return self._add_thumbnails(
                    r.json().get('artists', None),
                    self.filters.get('type', None)
                )
            elif self.filters.get('type', None) == 'album':
                return self._add_thumbnails(
                    r.json().get('albums', None),
                    self.filters.get('type', None)
                )
            elif self.filters.get('type', None) == 'playlist':
                return self._add_thumbnails(
                    r.json().get('playlists', None),
                    self.filters.get('type', None)
                )
            elif self.filters.get('type', None) == 'track':
                return self._add_thumbnails(
                    r.json().get('tracks', None),
                    self.filters.get('type', None)
                )

        return []
