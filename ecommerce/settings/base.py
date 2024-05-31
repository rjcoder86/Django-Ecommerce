from datetime import timedelta
import os

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'ks2zg!5l!0w#qwwp_=l*q*vio-!yxioq6n#qo_pzo5to77f2n-')

DEBUG = False if os.environ.get('PRODUCTION') == '1' else True

ALLOWED_HOSTS = ['localhost',  '127.0.0.1']

INSTALLED_APPS = [
    # in-build apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # custom apps
    'accounts',
    'billing',
    'products',
    'cart',
    'order',
    'users',

    # installed apps
    'rest_framework',
    'corsheaders',
    'rest_framework_simplejwt',
    'ckeditor'
]

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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'staticfiles')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Rest Framework Settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'AUTH_COOKIE': 'auth_token',  # Custom settings
    'AUTH_COOKIE_SECURE': False,
    'AUTH_COOKIE_HTTP_ONLY': True,
    'AUTH_COOKIE_PATH': '/',
    'AUTH_COOKIE_SAMESITE': 'Lax',
}
# Email Settings
SEND_GRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SEND_GRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'your email id'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


MANAGERS = (
    ('rohitdjadhav789@gmail.com', 'Rohit Jadhav'),
)

ADMINS = (
    ('rohitdjadhav789@gmail.com', 'Rohit Jadhav'),
)

# Static File Settings
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'project_static'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Razorpay Settings
CURRENCY = {
    'code': 'INR',
    'symbol': '₹'
}

RAZORPAY_KEY_ID = os.environ.get('RAZORPAY_KEY_ID')
RAZORPAY_KEY_SECRET = os.environ.get('RAZORPAY_KEY_SECRET')


# This will Help django To Log To Console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEBUG_PROPAGATE_EXCEPTIONS = True

# CORS Settings
CORS_ORIGIN_ALLOW_ALL = True

# STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY', '')
STRIPE_TEST_API_KEY = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

