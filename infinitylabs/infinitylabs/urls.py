from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_view),
    url(r'^home/$', index),
    url(r'^auth_view/$', auth_view),
    url(r'^router_details/$', router_details),
    url(r'^save/router/details/$', save_router_details),
    url(r'^delete/router/details/$', delete_router_details),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
