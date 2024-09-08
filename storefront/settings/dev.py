from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'

if DEBUG:
    MIDDLEWARE += ['silk.middleware.SilkyMiddleware',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'mysql',
        'USER': 'root',
        'PASSWORD': 'Burger408!'
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525

CELERY_BROKER_URL = 'redis://redis:6379/1' # 1 is set as our message broker

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": "redis://redis:6379/2", # Database 2 because 1 is already used by Celery
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True # We just need a function that returns True here
}