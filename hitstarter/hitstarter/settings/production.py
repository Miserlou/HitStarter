from hitstarter.settings.base import *

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS += ('sentry,')

DATABASES['default']['NAME'] = 'hitstarter_production'

SENTRY_LOG_DIR = os.path.join(PROJECT_DIR, 'logs')
SENTRY_RUN_DIR= os.path.join(PROJECT_DIR, 'run')
SENTRY_WEB_HOST = '127.0.0.1'
SENTRY_WEB_PORT = 9000
SENTRY_KEY = 'k3ah7*u9(z&o+0doiu@#(_z5-b@rgk9y!4@=i2ce3w%63p1^0q'

SENTRY_FILTERS = (
    'sentry.filters.StatusFilter',
    'sentry.filters.LoggerFilter',
    'sentry.filters.LevelFilter',
    'sentry.filters.ServerNameFilter',
    'sentry.filters.SiteFilter',
)

SENTRY_VIEWS = (
    'sentry.views.Exception',
    'sentry.views.Message',
    'sentry.views.Query',
)


