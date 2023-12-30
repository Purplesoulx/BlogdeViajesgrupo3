from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['rodrigofer.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'RodrigoFer$default',
        'USER': 'RodrigoFer',
        'PASSWORD': 'bloggrupo3',
        'HOST': 'RodrigoFer.mysql.pythonanywhere-services.com',
        'PORT': '',
    }
}