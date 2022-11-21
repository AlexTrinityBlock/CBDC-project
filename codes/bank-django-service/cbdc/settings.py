"""
Django settings for cbdc project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['BANK_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    os.environ['BANK_DJANGO_SERVICE_IP'],
]


# Application definition

INSTALLED_APPS = [
    # 手動添加的APP
    "corsheaders",
    'app_core.apps.AppCoreConfig',
    # 原生的APP
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware", # CORS 手動添加
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', # 開發時取消CSRF，開發完畢後加回去。
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app_core.middlewares.LoginMiddleware.LoginMiddleware', # 手動添加，登入中間層。
    'app_core.middlewares.PostHandler.PostHandler',
]

ROOT_URLCONF = 'cbdc.urls'

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

WSGI_APPLICATION = 'cbdc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# os.environ['REDIS_IP']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #MySQL
        'NAME': os.environ['MYSQL_DATABASE'],   #資料庫名稱                
        'USER': os.environ['MYSQL_USER'],       #管理員
        'PASSWORD': os.environ['MYSQL_PASSWORD'],#密碼
        'HOST': os.environ['MYSQL_IP'],          #資料庫IP
        'PORT': '3306',                       
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 允取特定IP的 Request
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8085",
    "http://127.0.0.1:8085",
    os.environ['USER_CRYPTOGRAPHY_SUPPORT_FLASK_SERVICE_URL'],
]