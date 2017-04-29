MyLittleJob Spotify Search
==========================

Get search results from Spotify Search API. Results can be filtered by artist, playlist, album or track. Written in Django.

## Features

* Unit tests.
* 88% test coverage.
* `django-environ` to manage enviroment variables.
* Search URLs can be copied.
* Filtering by 4 categories (artist, playlist, track, album).

Settings files are at `config/settings/`.

## Installing Dependencies

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

The contents of the `.env` file for `django-environ` is inside `prod.env`. So, while doing production deployment, rename `prod.env` to `.env` like so:
```
mv config/settings/prod.env config/settings/.env
```
Then,

```
export DJANGO_DEBUG=False
python manage.py collectstatic
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
