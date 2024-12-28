import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'ghn4j6$ya0(@rt0m%8v^9k@p&#$^dhky+7a*vzk_we73!=y^*_'

DEBUG = True

ALLOWED_HOSTS = ['localhost', 'https://www.googleapis.com/plus/v1/people/me','127.0.0.1']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'storage/cache'),
    }
}

INSTALLED_APPS = [
    'PIL',
    'weasyprint',
    'xlsxwriter',
    'ckeditor',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'recepie',
    'social_django',
]

MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recepie.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "recepie/templates")
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <- Here
                'social_django.context_processors.login_redirect', # <- Here
            ],
        },
    },
]

WSGI_APPLICATION = 'recepie.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_HOST_USER = 'tonmoyk983@gmail.com'
EMAIL_HOST_PASSWORD = '125805687Ton@#'


LOGIN_REDIRECT_URL = 'Profile'
LOGIN_URL = 'Login'
LOGOUT_REDIRECT_URL = 'Home'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_ROOT = '/recepie/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'storage/media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "recepie/static/recepie"),
    os.path.join(BASE_DIR,'recepie/static'),
    os.path.join(BASE_DIR, 'static'),
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CKEDITOR_BASEPATH = "/static/blog/ckeditor/ckeditor/"

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 'social_core.backends.github.GithubOAuth2',  # for Github authentication
 'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
 'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = 'Ov23liEGW1URh8adEwkj'
SOCIAL_AUTH_GITHUB_SECRET = '6d0b1bc7df27ff36cf6a3c921bde8745c7d2be3e'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '494874810472-igkvqb4ma8io2bqbt22c1etmuoebrvia.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'RHc7QVo_rJTnAuN7fOHuNWuo'

SOCIAL_AUTH_FACEBOOK_KEY = '1229977887153000'
SOCIAL_AUTH_FACEBOOK_SECRET = 'ac29f41481a71bfbac91730255024d1c'
