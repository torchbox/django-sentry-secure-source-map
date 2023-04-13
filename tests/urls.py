import re

from django.conf import settings
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    # To satisfy tests
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")),
        serve,
        {"document_root": settings.STATIC_ROOT},
    )
]
