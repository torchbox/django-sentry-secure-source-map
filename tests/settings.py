import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "tests",
    "django_sentry_protect",
]

MIDDLEWARE = ["django_sentry_protect.SentryProtectMiddleware"]

SECRET_KEY = "abcde12345"

STATIC_ROOT = os.path.join(BASE_DIR, "tests", "collected-static")
STATIC_URL = "/static/"

USE_TZ = False

ROOT_URLCONF = "tests.urls"


SENTRY_SECURITY_TOKEN = "sentry-token"
SENTRY_PROTECTED_PATHS = [re.escape(STATIC_URL) + r".+\.map$"]
