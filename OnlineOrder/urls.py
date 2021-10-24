from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.urls import path
from . import views


urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('order', views.order, name='order'),
]