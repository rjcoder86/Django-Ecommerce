from .base import *

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'ecom_db',

        'USER': 'postgres',

        'PASSWORD': 'keywordio2022',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}
SECRET_KEY = 'ly19&2+c#onohxpodxnrlpvx3#)wc_qw!nvnb0^)oe%_yj$vf4'
ALLOWED_HOSTS = ['*']

MEDIA_ROOT = '/home/ecommerce/ecommerce/media'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/ecommerce/ecommerce/static'
STATIC_URL = '/static/'
