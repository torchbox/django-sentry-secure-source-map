import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "tests",
    "sentry_secure_source_map",
]

MIDDLEWARE = ["sentry_secure_source_map.SentrySecureSourceMapMiddleware"]

SECRET_KEY = "abcde12345"

STATIC_ROOT = os.path.join(BASE_DIR, "tests", "static")
STATIC_URL = "/static/"

USE_TZ = False

ROOT_URLCONF = "tests.urls"


SENTRY_SECURITY_TOKEN = "sentry-token"
