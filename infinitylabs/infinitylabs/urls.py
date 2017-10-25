from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^landing_page/$', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
