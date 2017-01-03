from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<location_id>[0-9]+)/$', views.location, name='location'),
    url(r'^(?P<location_id>[0-9]+)/(?P<cart_id>[0-9]+)/$', views.cart, name='cart'),
    url(r'^(?P<location_id>[0-9]+)/(?P<cart_id>[0-9]+)/(?P<service_id>[0-9]+)/$', views.service, name='service'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)