import re

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http import HttpResponseForbidden
from django.utils.crypto import constant_time_compare


class SentryProtectMiddleware:
    def __init__(self, get_response):
        if not settings.SENTRY_SECURITY_TOKEN:
            raise MiddlewareNotUsed

        self.protected_paths = [
            re.compile(protected_path)
            for protected_path in getattr(settings, "SENTRY_PROTECTED_PATHS", [])
        ]

        self.get_response = get_response

    def __call__(self, request):
        is_protected = any(
            protected_path.search(request.path)
            for protected_path in self.protected_paths
        )

        if is_protected:
            sentry_token = request.headers.get("X-Sentry-Token", "")

            if not constant_time_compare(sentry_token, settings.SENTRY_SECURITY_TOKEN):
                return HttpResponseForbidden()

        return self.get_response(request)
