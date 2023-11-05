from pathlib import Path
import os

if os.name == 'nt':
    VENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VENV_BASE, 'Lib\\site-packages\\osgeo\\data\\proj') + ';' + os.environ['PATH']
    
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r@4rz6+o4m*@$u_yt=8o!)9f6!j&p)7i_q*0r9$74rb&4)2-ml'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['docker-test-yb57.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'api',
    'rest_framework_gis',
    'rest_framework',
    'leaflet',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True


STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': 'barangay_api_db',
#         'USER': 'postgres',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         'CONN_MAX_AGE': 60,
#     }
# }   


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.contrib.gis.db.backends.postgis',
#         'NAME': '',
#         'USER': 'postgres',
#         'PASSWORD': 'Janjan_12345',
#         'HOST': '',
#         'PORT': '5432',
#     }
# }


# import environ
# import dj_database_url
# env = environ.Env()
# environ.Env.read_env()

# db_config = dj_database_url.parse(env('DATABASE_URL'))
# db_config['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# db_config['CONN_MAX_AGE'] = 600

# DATABASES = {
#     'default': db_config
# }


# import environ
# import dj_database_url
# env = environ.Env()
# environ.Env.read_env()

# db_config = dj_database_url.parse('postgres://barangay_api_db_user:15Nr2Ggg1OGmLaQHADXTa2TYaOdItwLM@dpg-cjbibjrbq8nc73d3cc40-a.singapore-postgres.render.com/barangay_api_db')
# db_config['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
# db_config['CONN_MAX_AGE'] = 60

# DATABASES = {
#     'default': db_config
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'barangay_db_z9pu',
        'USER': 'barangay_db_z9pu_user',
        'PASSWORD': 'DFIRnPvCRUCg6Xt0WNu5i6gCaWVmJFnO',
        'HOST': 'dpg-cl33tt8t3kic73d6ktl0-a.oregon-postgres.render.com',
        'PORT': 5432,
        'CONN_MAX_AGE': 60,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

CSRF_TRUSTED_ORIGINS = ['https://docker-test-yb57.onrender.com']


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = 'static/'
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LEAFLET_CONFIG = {
    'DEFAULT_CENTER' : (11.5833,124.4642),
    'DEFAULT_ZOOM': 10,
    'MIN_ZOOM': 10,
    'MAX_ZOOM': 19,
    'ATTRIBUTION_PREFIX': 'GEOSPATIAL DATA ANALYSIS',
    'RESET_VIEW' : True,
    
    'SPATIAL_EXTENT': (124.04521599909879, 11.438789761131503, 124.80435303834872, 11.845561820416577),
}
