from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("accounts.urls")),
    path("", include("home.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)