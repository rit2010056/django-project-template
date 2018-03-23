"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import logging
logger = logging.getLogger(__name__)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    # project apps
    'django_project',

    # vendor apps (project specific)

    # vendor apps
    # 'corsheaders',
    # 'easy_thumbnails',
    # 'fancybox',
    # 'import_export',
    'loginas',
    # 'oauth2_provider',
    # 'rest_framework',
    'theme_microdisseny',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # vendor apps that depend on django apps
    'groupadmin_users',
]

MIDDLEWARE = [
    # request logging
    # 'request_logging.middleware.LoggingMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # cors headers
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': os.getenv('TEMPLATES', '').split(','),
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

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        # 'ENGINE': 'django.db.backends.postgresql',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': os.environ.get('DB_NAME', ''),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# General
# DEBUG defaults to False if not defined in the environment
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# e.g.: My name,admin@example.com,Other admin,admin2@example.com
# ADMINS will be an empty array is it is not defined in the environment
ADMINS = zip(*([iter(os.getenv('ADMINS', '').split(','))]*2))

LANGUAGE_CODE = 'ca'
LANGUAGE_CODE = os.getenv('LANGUAGE_CODE', LANGUAGE_CODE)

TIME_ZONE = 'Europe/Madrid'
TIME_ZONE = os.getenv('TIME_ZONE', TIME_ZONE)

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_URL = os.getenv('SITE_URL')

APP_NAME = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.getenv('APP_NAME', APP_NAME)

APP_URL = '/apps/%s/' % APP_NAME
APP_URL = os.getenv('APP_URL', APP_URL)
APP_ROOT = os.getenv('APP_PATH', BASE_DIR)

LOGIN_URL = '%s/admin/login/' % APP_URL
LOGIN_REDIRECT_URL = '%s/admin/' % APP_URL

MEDIA_URL = '%s/media/' % APP_URL
MEDIA_URL = os.getenv('MEDIA_URL', MEDIA_URL)
MEDIA_ROOT = os.path.join(APP_ROOT, 'media')
MEDIA_ROOT = os.getenv('MEDIA_ROOT', MEDIA_ROOT)

STATIC_URL = '%s/static/' % APP_URL
STATIC_URL = os.getenv('STATIC_URL', STATIC_URL)
STATIC_ROOT = os.path.join(APP_ROOT, 'static')
STATIC_ROOT = os.getenv('STATIC_ROOT', STATIC_ROOT)

SESSION_COOKIE_NAME = 'sessionid_%s' % APP_URL.replace('/', '_')
SESSION_COOKIE_PATH = '%s/' % APP_URL

LOCALE_PATHS = [
    os.path.join(APP_ROOT, 'locale'),
]

EMAIL_SUBJECT_PREFIX = '[%s] ' % APP_NAME
# From address for error messages
SERVER_EMAIL = os.getenv('SERVER_EMAIL', '')

# corsheaders
# CORS_ORIGIN_ALLOW_ALL = os.getenv('CORS_ORIGIN_ALLOW_ALL',
#                                   'False').lower() == 'true'
# CORS_ORIGIN_WHITELIST = (
#     'www.example.com',
# )
# CORS_ALLOW_CREDENTIALS = True


# easy-thumbnails
# THUMBNAIL_BASEDIR = 'thumbs'
# THUMBNAIL_ALIASES = {
#     '': {
#         'changelist': {'size': (50, 50), 'crop': False},
#     },
# }


# oauth-toolkit
# AUTHENTICATION_BACKENDS = (
#     'oauth2_provider.backends.OAuth2Backend',
#     # Uncomment following if you want to access the admin
#     'django.contrib.auth.backends.ModelBackend'
# )

# index = MIDDLEWARE.index('django.contrib.auth.middleware.'
#                          'AuthenticationMiddleware')
# MIDDLEWARE.insert(index + 1,
#                   'oauth2_provider.middleware.OAuth2TokenMiddleware')

# OAUTH2_PROVIDER = {
#     # Authentication server needs the introspection scope
#     # 'SCOPES': {
#     #     'read': 'Read scope',
#     #     'write': 'Write scope',
#     #     'introspection': 'Introspect token scope',
#     # },
# 
#     # Resource server delegating auth to Authentication server
#     # 'RESOURCE_SERVER_INTROSPECTION_URL': 'https://example.org/o/introspect/',
#     # 'RESOURCE_SERVER_INTROSPECTION_URL':
#     #     os.environ.get('RESOURCE_SERVER_INTROSPECTION_URL'),
#     # 'RESOURCE_SERVER_AUTH_TOKEN': os.environ.get('RESOURCE_SERVER_AUTH_TOKEN'),
#     # 'RESOURCE_SERVER_TOKEN_CACHING_SECONDS': 60 * 60 * 10,
# 
#     'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 24 * 365 * 10,
# }


# rest-framework
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         # 'rest_framework.authentication.BasicAuthentication',
#         'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': [
#         # Require a valid user
#         'rest_framework.permissions.IsAuthenticated',
#         # Warning: Staff (admin) user required:
#         # 'rest_framework.permissions.IsAdminUser',
#         # Warning: GET is not protected, open to authenticated users
#         # 'rest_framework.permissions.DjangoModelPermissions',
#         # default setting:
#         'rest_framework.permissions.AllowAny',
#     ],
#     # 'DEFAULT_RENDERER_CLASSES': (
#     #     'drf_ujson.renderers.UJSONRenderer',
#     # ),
#     # 'DEFAULT_PARSER_CLASSES': (
#     #     'drf_ujson.parsers.UJSONParser',
#     # ),
#     'PAGE_SIZE': 100
# }


# request-logging
REQUEST_LOGGING_DATA_LOG_LEVEL = logging.DEBUG
LOG_LEVEL = os.getenv('REQUEST_LOGGING_DATA_LOG_LEVEL')
if LOG_LEVEL in ('DEBUG', 'INFO', 'WARN', 'ERROR'):
    REQUEST_LOGGING_DATA_LOG_LEVEL = getattr(logging, LOG_LEVEL)
else:
    logger.error('REQUEST_LOGGING_DATA_LOG_LEVEL value not valid: %s'
                 % LOG_LEVEL)
REQUEST_LOGGING_ENABLE_COLORIZE = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        # django request
        # 'django.request': {
        #     'handlers': ['console'],
        #     'level': 'INFO',  # change debug level as appropiate
        #     'propagate': False,
        # },
    },
}


# Overwrite settings using ENVIRONMENT_NAME
ENVIRONMENT_NAME = os.environ.get('ENVIRONMENT_NAME', '')
extra_settings_file = 'settings-%s.py' % ENVIRONMENT_NAME
extra_settings_dir = os.path.dirname(os.path.abspath(__file__))
extra_settings_path = os.path.join(extra_settings_dir, extra_settings_file)
if os.path.exists(extra_settings_path):
    try:
        exec(compile(
            open(
                extra_settings_path, "rb"
            ).read(), extra_settings_path, 'exec'), globals())
    except Exception as e:
        raise Exception(
            "Failed to import extra settings from %s" % extra_settings_path
         )
# FIXME: python3 only
#        ) from exc
