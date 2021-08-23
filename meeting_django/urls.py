"""Handle all endpoints from system."""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from workshop.views import home_page, get_dashboard_partials
from workshop.views import create_participant


urlpatterns = [
    path('admin/', admin.site.urls),
    url('partials', get_dashboard_partials, name='partials'),
    url('participant', create_participant, name='participant'),
    url(r'^$', home_page, name='home_page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
