from __future__ import unicode_literals
"""
Django settings for myshop project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decimal import Decimal
from django.utils.translation import ugettext_lazy as _

# Patches backported from Django<1.8
from django.utils import numberformat
from shop.patches import numberformat as patched_numberformat
numberformat.format = patched_numberformat.format

SHOP_APP_LABEL = 'myshop'
BASE_DIR = os.path.dirname(__file__)

# Directory where working files, such as media and databases are kept
WORK_DIR = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir, os.path.pardir, 'workdir'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

ADMINS = ((u'The Merchant', u'the.merchant@example.com'),)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nqniwbt=%@5a(e8%&h#c^0()64(ujs0=4%_nyajn*t6a$ca&at'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Application definition

# replace django.contrib.auth.models.User by implementation
# allowing to login via email address
AUTH_USER_MODEL = 'email_auth.User'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'email_auth',
    'polymorphic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'djangocms_text_ckeditor',
    'django_select2',
    'cmsplugin_cascade',
    'cmsplugin_cascade.sharable',
    'cmsplugin_cascade.extra_fields',
    'cmsplugin_cascade.segmentation',
    'cms_bootstrap3',
    'adminsortable2',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'fsm_admin',
    'djangular',
    'cms',
    'menus',
    'treebeard',
    'nodebow',
    'compressor',
    'sekizai',
    'sass_processor',
    'django_filters',
    'filer',
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    'parler',
    'reversion',
    'post_office',
    'haystack',
    'shop',
    'myshop',
)

MIDDLEWARE_CLASSES = (
    'djangular.middleware.DjangularUrlMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'shop.middleware.CustomerMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'myshop.urls'

WSGI_APPLICATION = 'myshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(WORK_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'de'

LANGUAGES = (
    ('en', "English"),
    ('de', "Deutsch"),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_X_FORWARDED_HOST = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(WORK_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory that holds static files.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(WORK_DIR, 'static')

# URL that handles the static files served from STATIC_ROOT.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
    'compressor.finders.CompressorFinder',
    'nodebow.finders.BowerComponentsFinder',
)

STATICFILES_DIRS = (
    os.path.join(WORK_DIR, 'static'),
)


# URL prefix for admin media -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.cms_settings',
    'shop.context_processors.customer',
    'stofferia.context_processors.global_context',
    'sekizai.context_processors.sekizai',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

SECURE_PROXY_SSL_HEADER = (u'HTTP_X_FORWARDED_PROTO', u'https')

TEMPLATE_DEBUG = DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s %(module)s] %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}


############################################
# settings for sending mail

EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@example.com'
EMAIL_HOST_PASSWORD = 'smtp-secret-password'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'My Shop <no-reply@example.com>'
EMAIL_REPLY_TO = 'info@example.com'
EMAIL_BACKEND = 'post_office.EmailBackend'


############################################
# settings for third party Django apps

NODEBOW_ROOT = WORK_DIR

COERCE_DECIMAL_TO_STRING = True

COMPRESS_ENABLED = True

FSM_ADMIN_FORCE_PERMIT = True

PARLER_DEFAULT_LANGUAGE = 'de'

PARLER_LANGUAGES = {
    1: (
        {'code': 'de'},
        {'code': 'en'},
    ),
    'default': {
        'fallbacks': ['de', 'en'],
    },
}

SASS_PROCESSOR_INCLUDE_DIRS = (
    #os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'node_modules/bootstrap-sass/assets/stylesheets')),
    #os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'node_modules/compass-mixins/lib')),
    os.path.abspath(os.path.join(BASE_DIR, os.pardir, 'node_modules')),
)


############################################
# settings for django-restframework and plugins

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'shop.rest.money.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',  # can be disabled for production environments
    ),
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.authentication.TokenAuthentication',
#    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGINATE_BY': 16,
    'MAX_PAGINATE_BY': 100,
}

SERIALIZATION_MODULES = {'shop': b'shop.money.serializers'}


############################################
# settings for storing data in memory

X_CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'KEY_PREFIX': SHOP_APP_LABEL + '-cache',
    },
}

SESSION_ENGINE = 'redis_sessions.session'
SESSION_SAVE_EVERY_REQUEST = True
SESSION_REDIS_PREFIX = SHOP_APP_LABEL + '-session'


############################################
# settings for storing files and images

FILER_ADMIN_ICON_SIZES = ('16', '32', '48', '80', '128')

FILER_ALLOW_REGULAR_USERS_TO_ADD_ROOT_FOLDERS = True

FILER_DUMP_PAYLOAD = False

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880

THUMBNAIL_HIGH_RESOLUTION = False

THUMBNAIL_OPTIMIZE_COMMAND = {
    'gif': '/opt/local/bin/optipng {filename}',
    'jpeg': '/opt/local/bin/jpegoptim {filename}',
    'png': '/opt/local/bin/optipng {filename}'
}

THUMBNAIL_PRESERVE_EXTENSIONS = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


############################################
# settings for django-cms and its plugins

CMS_TEMPLATES = (
    ('myshop/pages/default.html', _("Default Page")),
#    ('myshop/pages/cart-checkout-view.html', _("Cart & Checkout View")),
#    ('myshop/pages/order-views.html', _("Order Views")),
#    ('myshop/pages/search-view.html', _("Search View")),
#    ('myshop/pages/catalog-list-commodity.html', _("Commodity List View")),
)

CMS_SEO_FIELDS = True

CMS_LANGUAGES = {
    'default': {
        'fallbacks': ['de', 'en'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
    1: ({
        'public': True,
        'code': 'de',
        'hide_untranslated': False,
        'name': 'Deutsch',
        'redirect_on_fallback': True,
    }, {
        'public': True,
        'code': 'en',
        'hide_untranslated': False,
        'name': 'English',
        'redirect_on_fallback': True,
    },)
}

CMS_CACHE_DURATIONS = {
    'content': 600,
    'menus': 3600,
    'permissions': 86400,
}

CMS_PERMISSION = False

CMSPLUGIN_CASCADE_PLUGINS = ('cmsplugin_cascade.segmentation', 'cmsplugin_cascade.generic', 'cmsplugin_cascade.link', 'shop.cascade', 'cmsplugin_cascade.bootstrap3',)

CMSPLUGIN_CASCADE_DEPENDENCIES = {
    'shop/js/admin/shoplinkplugin.js': 'cascade/js/admin/linkpluginbase.js',
}

CMSPLUGIN_CASCADE_ALIEN_PLUGINS = ('TextPlugin', 'TextLinkPlugin',)

CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES = (
    'shop.cascade.plugin_base.CatalogLinkPluginBase',
    'cmsplugin_cascade.link.plugin_base.LinkElementMixin',
    'shop.cascade.plugin_base.CatalogLinkForm',
)

CMSPLUGIN_CASCADE_WITH_EXTRAFIELDS = (
    'BootstrapButtonPlugin',
    'BootstrapRowPlugin',
    'SimpleWrapperPlugin',
    'HorizontalRulePlugin',
    'ExtraAnnotationFormPlugin',
)

CMSPLUGIN_CASCADE_SEGMENTATION_MIXINS = (
    ('cmsplugin_cascade.segmentation.mixins.SegmentPluginModelMixin', 'cmsplugin_cascade.segmentation.mixins.EmulateUserAdminMixin'),
)

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'skin': 'moono',
    'toolbar': 'CMS',
    'toolbar_HTMLField': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
        ['Maximize', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight'],
        ['HorizontalRule'],
        ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
        ['Source']
    ],
}

#############################################
# settings for full index text search (Haystack)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'stofferia-de',
    },
    'en': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://localhost:9200/',
        'INDEX_NAME': 'stofferia-en',
    },
}

HAYSTACK_ROUTERS = ('shop.search.routers.LanguageRouter',)

############################################
# settings for django-shop and its plugins

SHOP_VALUE_ADDED_TAX = Decimal(19)
SHOP_DEFAULT_CURRENCY = 'EUR'
SHOP_CART_MODIFIERS = (
    'shop.modifiers.defaults.DefaultCartModifier',
    'shop.modifiers.taxes.CartExcludedTaxModifier',
    'myshop.modifiers.PostalShippingModifier',
    'shop.modifiers.defaults.PayInAdvanceModifier',
    #'stofferia.stripe_payment.StripePaymentModifier',
)
SHOP_EDITCART_NG_MODEL_OPTIONS = "{updateOn: 'default blur', debounce: {'default': 2500, 'blur': 0}}"

SHOP_ORDER_WORKFLOWS = (
    'shop.payment.defaults.PayInAdvanceWorkflowMixin',
    'shop.payment.defaults.CommissionGoodsWorkflowMixin',
    #'stofferia.stripe_payment.OrderWorkflowMixin',
)

SHOP_STRIPE = {
    'PUBKEY': 'pk_test_stripe_secret',
    'APIKEY': 'sk_test_stripe_secret',
    'PURCHASE_DESCRIPTION': _("Thank for purchasing at MyShop"),
}
