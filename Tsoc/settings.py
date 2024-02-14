from pathlib import Path
import os
import boto3

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'bs3$b(+5vqe(=#+5-#p0v6fz9_d)creqg-1ql7exyn18&yx=cu'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tango',
    'captcha',
    'storages',
    'boto3'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Tsoc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'tango/templates')],
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

WSGI_APPLICATION = 'Tsoc.wsgi.application'

CSRF_TRUSTED_ORIGINS = [
    'https://www.tangosixoclock.in',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'deltatsoc',
#         'USER': 'postgres',
#         'PASSWORD': 'Django123',
#         'HOST': 'window-db.cpzckj1ocmci.ap-south-1.rds.amazonaws.com',
#         'PORT': '5432',
#     }
# }

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR,"static/images/")



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_USE_TLS = True 

EMAIL_HOST_USER = 'tangosixoclock@gmail.com'
EMAIL_HOST_PASSWORD = 'qlpe ihcc juvi fomm'

DEFAULT_FROM_EMAIL = 'tangosixoclock@gmail.com'

EMAIL_TIMEOUT = 10

# APPEND_SLASH = False

# test payment api
# KEY_ID = 'rzp_test_F8MIMQQ24shScO'
# KEY_SECRET = 'RF8VtlBN01wRgcOTnO6OqUnL'

AWS_ACCESS_KEY_ID = 'AKIA3J2PI5IBCMJAUV7L'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'tangowindows'
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


# live payment api
KEY_ID = 'rzp_live_0JNj8abM7pJbL3'
KEY_SECRET = 'xH8MJ0DQ7GwYZ6z0zLdK7JY5'
