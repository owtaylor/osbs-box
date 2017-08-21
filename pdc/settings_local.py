# Feel free to `cp settings_local.py.dist settings.local.py`
# and customize your settings, changes here will be populated
# automatically.
#
# This file only contains the minimized settings you should do,
# please look into settings.py to see the whole avaiable settings
# you can do for your PDC instance.
#
# NOTE: For developers or others who want to extend the default
#       settings, please remember to update your settings_local.py
#       when the items you extended got updated in settings.py.
#
# Example 1: if you want to enable `debug_toolbar` and
# `django_extensions` in INSTALLED_APPS, please remember
# to also include all the other apps listed in the settings.py,
# otherwise, the missed apps will not get installed.
#
#     INSTALLED_APPS = (
#         ...
#
#         'django_extensions',
#         'debug_toolbar',
#     )
#
# Example 2: when you run PDC locally, you may not want to enable
# the permission check system of the `REST_FRAMEWORK`, to do
# this, just need to comment out the `DEFAULT_PERMISSION_CLASSES`
# section.
#
#     REST_FRAMEWORK = {
#         'DEFAULT_AUTHENTICATION_CLASSES': (
#             'pdc.apps.auth.authentication.TokenAuthenticationWithChangeSet',
#             'rest_framework.authentication.SessionAuthentication',
#         ),
#
#     #    'DEFAULT_PERMISSION_CLASSES': [
#     #        'rest_framework.permissions.DjangoModelPermissions'
#     #    ],
#
#         'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',
#                                     'pdc.apps.utils.utils.RelatedNestedOrderingFilter'),
#
#         'DEFAULT_METADATA_CLASS': 'contrib.bulk_operations.metadata.BulkMetadata',
#
#         'DEFAULT_RENDERER_CLASSES': (
#             'rest_framework.renderers.JSONRenderer',
#             'pdc.apps.common.renderers.ReadOnlyBrowsableAPIRenderer',
#         ),
#
#         'EXCEPTION_HANDLER': 'pdc.apps.common.handlers.exception_handler',
#
#         'DEFAULT_PAGINATION_CLASS': 'pdc.apps.common.pagination.AutoDetectedPageNumberPagination',
#     }


import os.path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

# NOTE: this is needed when DEGUB is False.
#       https://docs.djangoproject.com/en/1.8/ref/settings/#allowed-hosts
# E.g.
#     ALLOWED_HOSTS = ['pdc.example.com']
ALLOWED_HOSTS = ['pdc']

AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.RemoteUserBackend',
    'pdc.apps.auth.backends.AuthMellonUserBackend',
)

# ADMINS and MANAGERS
# ADMINS = ()
# MANAGERS = ADMINS

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':  'pdc',
        'USER': 'koji',
        'PASSWORD': 'mypassword',
        'HOST': 'koji-db',
        'PORT': '5432',
    }
}

REST_API_URL = 'rest_api/'
REST_API_VERSION = 'v1'

BROWSABLE_DOCUMENT_MACROS = {
    # need to be rewrite with the real host name when deploy.
    'HOST_NAME': 'http://pdc',
    # make consistent with rest api root.
    'API_PATH': '%s%s' % (REST_API_URL, REST_API_VERSION),
}

def get_setting(setting):
    import settings
    return getattr(settings, setting)

# ======== Email configuration =========
# Email addresses who would like to receive email
#ADMINS = (('PDC Dev', 'pdc@example.com'),)
ADMINS = ()
# Email SMTP HOST configuration
#EMAIL_HOST = 'smtp.example.com'
# Email sender's address
#SERVER_EMAIL = 'noreply@example.com'
#EMAIL_SUBJECT_PREFIX = '[PDC]'

# un-comment below 4 lines if enable email notification as meet any error
# get_setting('LOGGING').get('loggers').update({'pdc.apps.common.handlers': {
#     'handlers': ['mail_admins'],
#     'level': 'ERROR',
# }})