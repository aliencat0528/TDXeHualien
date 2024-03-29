"""
Django settings for eHualien project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#BASE_DIR = Path(__file__).resolve().parent
#print(BASE_DIR)
#print(str(BASE_DIR / 'db.sqlite3'))
#print(str(BASE_DIR / 'tdxDemo'/'models.py'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g4fb9rj5u4oh_3uvdx^nl(^88p+)liunj5wbd@%=!2op++01ux'
LINE_CHANNEL_ACCESS_TOKEN='+NxQ7iYuVGOD7rrUF/zr7tvFSjv8AKA60Y1WcoIY2Th6XuBPzVAeC5Vt/7TQZ7slJ6sw885hyTTw92foUMUzt7R1/1A7lZ6zmIELVmghZdr1bDfWTqdhxWTwmSGhRctkhdjk8ltJQ6RW1bC3ZSyXrgdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET='09431d7b4202329df7ed445834441afc'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'tdxDemo.models.parkInfoDB',
    'tdxDemo.apps.TdxDemoConfig'
    #'tdxDemo'

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

ROOT_URLCONF = 'eHualien.urls'

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

WSGI_APPLICATION = 'eHualien.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'parkdb',
        'USER': 'root',
        'PASSWORD': 'angel$SQL528',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': str(BASE_DIR / 'db.sqlite3'),
#    }
# }

#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',  #PostgreSQL
#         'NAME': 'tdxData',  #資料庫名稱
#         'USER': 'postgres',  #資料庫帳號
#         'PASSWORD': '0528',  #資料庫密碼
#         'HOST': 'localhost',  #Server(伺服器)位址
#         'PORT': '5432'  #PostgreSQL Port號
#     }
# }



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

LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
