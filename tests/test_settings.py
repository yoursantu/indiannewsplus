"""Settings that need to be set in order to run the tests."""
import os


DEBUG = True
USE_TZ = True

SITE_ID = 1
SECRET_KEY = 'secret_key_for_django'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_I18N = True

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('de', 'German'),
)

ROOT_URLCONF = 'multilingual_news.tests.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../media/')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'test_static'),
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': [os.path.join(os.path.dirname(__file__), '../templates')],
    'OPTIONS': {
        'context_processors': (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.i18n',
            'django.core.context_processors.request',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'sekizai.context_processors.sekizai',
        )
    }
}]

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    '__init__$', 'tests$', 'settings$', 'urls$', 'locale$',
    'south_migrations', 'fixtures', 'admin$', 'django_extensions',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'djangocms_text_ckeditor',  # must come before cms
    'cms',
    'djangocms_link',
    'django_libs',
    'sekizai',
    'menus',
    'mptt',
    'filer',
    'easy_thumbnails',
    'hvad',
    'document_library',
    'people',
    'multilingual_tags',
    'treebeard',
]

INTERNAL_APPS = [
    'multilingual_news.tests.test_app',
    'multilingual_news',
]

INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

CMS_SOFTROOT = True
CMS_PERMISSION = False
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_FRONTEND_LANGUAGES = ('en', 'de', )
CMS_TEMPLATES = (
    ('base.html', 'Standard'),
)

# settings for localized_names
LONG_NAME_FORMAT = '{g} {L}, {f}'
LONG_NAME_FORMAT_NON_ROMAN = '{g} {x}, {a} ({L}, {f})'
