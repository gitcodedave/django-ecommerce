import os

import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

REDIS_URL = os.environ['REDIS_URL']

ALLOWED_HOSTS = ['.davestore-prod-572ad197703b.herokuapp.com/']

DATABASES = {
    'default': dj_database_url.config()
}

EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']

CELERY_BROKER_URL = REDIS_URL # 1 is set as our message broker

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "TIMEOUT": 10 * 60,
        "LOCATION": REDIS_URL, # Database 2 because 1 is already used by Celery
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}