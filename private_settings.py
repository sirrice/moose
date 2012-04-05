import os
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.        
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'db.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

MEDIA_ROOT = '%s/media' % ROOT_PATH

STATIC_ROOT = '%s/static' % ROOT_PATH

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_ROOT,
)

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = '230p9g340py9g,34p0[9"#$Y<PY<$5y,43y,3$y3'

