from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from .views import LoginRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginRedirectView.as_view(), name = 'index'),
    path('user/', include('apps.user.urls')),
    path('polls/', include('apps.polls.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
