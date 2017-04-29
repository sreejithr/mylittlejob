MyLittleJob Spotify Search
==========================

Uses the Spotify Search API to get search results for terms. Results can be filtered by artist, playlist, album or track.

## Features

* Copy-able urls for searches.
* Filtering by 4 categories (artist, playlist, track, album).
* Unit tests.
* 88% test coverage.

## Installation

### Dev

```
pip install -r requirements.txt
```

## Production

```
pip install -r requirements/production.txt
```

## How to run

### Dev

```
python manage.py runserver
```

Now, browse to [http://localhost:8000/](http://localhost:8000/)!

### Production

```
export DJANGO_DEBUG=False
gunicorn config.wsgi
```
`localhost` is present in the `ALLOWED_HOSTS` setting. This was done for convenience.

Go to [http://localhost:8000/](http://localhost:8000/)!

## Testing & Coverage

You can run test cases like so:

```
coverage run python manage.py test --settings=config.settings.test
```

And get coverage reports like so:

```
coverage report
```
