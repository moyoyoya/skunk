from .base import *

DEBUG = True

ADMINS = (
    ('Ulises M.', 'ulises.moya@gmail.com'),
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Rigby',
        'USER': 'Rigby',
        'PASSWORD': '1234',
    }
}