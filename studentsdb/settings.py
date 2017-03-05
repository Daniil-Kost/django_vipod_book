"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os
import email

import json

from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '91i_4a-y_@q7i9*yxzzw^+xnh94h6n^j$2)o99cb27-t@ix@@w'

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
    'crispy_forms',
    'students',

]


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#i need to templeate in Middleware - 'django.middleware.locale.LocaleMiddleware',
#but after this, i must translate web-site to russian and english language 

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'studentsdb.urls'

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
                "django.core.context_processors.request",
                "studentsdb.context_processors.students_proc",
        "students.context_processors.groups_processor",
            ],
        },
    },
]

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR,'..','db.sqlite3'),
 #   }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': '12345678',
        'NAME': 'students_db',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

PORTAL_URL = 'http://localhost:8000'

MEDIA_URL ='/media/'

MEDIA_ROOT =os.path.join(BASE_DIR, '..', 'media')

#email settings
#please, set here your server details and your admin email
#ADMIN_EMAIL = 'lemk1997@gmail.com'
#EMAIL_HOST = 'smtp.mandrillapp.com'
#EMAIL_PORT = '465'
#EMAIL_HOST_USER = 'lemk1967@gmail.com'
#EMAIL_HOST_PASSWORD = '****' 
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = True
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMIN_EMAIL = 'lemk1997@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'lemk1997@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv('WEBSITE_PASS')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SITE_ID = 1
SERVER_EMAIL = "lemk1997@gmail.com"
DEFAULT_FROM_EMAIL = "admin@studentsdb.uk.to"
MANAGERS = [('admin','lemk1997@gmail.com')]
ADMINS = (
    ('admin', 'lemk1997@gmail.com'),
)






#MANAGERS = ADMINS

CRISPY_TEMPLATE_PACK ='bootstrap3'