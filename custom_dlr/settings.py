import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']  # Update for production

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'custom_dlr.urls'

WSGI_APPLICATION = 'custom_dlr.wsgi.application'

SCHEDULER = BackgroundScheduler()
SCHEDULER.start()
