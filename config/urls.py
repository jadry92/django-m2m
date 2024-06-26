"""
config URL Configuration
"""
# Django
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("account/", include("allauth.urls")),
    path("", include("music.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
