from django.urls import re_path
import re
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # To satisfy tests
    re_path(r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")), serve, {"document_root": settings.STATIC_ROOT})
]
