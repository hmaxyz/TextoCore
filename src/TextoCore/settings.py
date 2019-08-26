"""
Django settings for TextoCore project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sz8_@+^9a^@0)a!dake2f@-81yy^pg^4l(%in6eg#wbt4juk&r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'account',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TextoCore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'TextoCore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


EMAIL_HOST = os.environ.get('AWS_SES_HOST')
# "postmaster@sandbox9c88ec3096984f9e877105aeeb28877c.mailgun.org"

EMAIL_HOST_USER = os.environ.get('AWS_SES_USERNAME')
# "e75a529a3f87570f3d77ab9ac3319ff5-49a2671e-6400a9b7"
EMAIL_HOST_PASSWORD = os.environ.get('AWS_SES_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "noreply@alert.texto.com.ng"

SMS_SEND_ENPOINT = os.environ.get('SMS_SEND_ENPOINT')
SMS_BALANCE_ENPOINT = os.environ.get('SMS_BALANCE_ENPOINT')
SMS_RATE_ENPOINT = os.environ.get('SMS_RATE_ENPOINT')
SMS_USERNAME = os.environ.get('SMS_USERNAME')
SMS_PASSWORD = os.environ.get('SMS_PASSWORD')

SMS_RATE_API = ("{}?user={}&password={}").format(
    SMS_RATE_ENPOINT, SMS_USERNAME, SMS_PASSWORD)
SMS_BALANCE_API = ("{}?username={}&password={}").format(
    SMS_BALANCE_ENPOINT, SMS_USERNAME, SMS_PASSWORD)
SMS_SEND_API = ("{}?username={}&password={}&").format(
    SMS_SEND_ENPOINT, SMS_USERNAME, SMS_PASSWORD)
