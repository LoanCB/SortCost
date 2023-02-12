from .base import *

DEBUG = True
DJANGO_VITE_DEV_MODE = DEBUG
CURRENT_IP = '192.168.7.194'
SITE_URL = 'http://127.0.0.1:8000'

ALLOWED_HOSTS = ['127.0.0.1', CURRENT_IP]
INTERNAL_IPS = ALLOWED_HOSTS

DATABASES['default']['NAME'] = 'sortcost_dev'
DATABASES['default']['USER'] = 'postgres'
DATABASES['default']['PASSWORD'] = os.getenv('DATABASE_PASSWORD')

CORS_ORIGIN_ALLOW_ALL = True
