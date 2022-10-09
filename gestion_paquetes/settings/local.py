from .base import *


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'paquete',
        'USER': 'postgres',
        'PASSWORD': 'Tascon1234W',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

CORS_ORIGIN_ALLOW_ALL = True 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


STATIC_URL = 'static/'