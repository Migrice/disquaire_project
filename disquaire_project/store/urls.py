from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    url(r'^search/$',views.search ,name="search"),#  route pour afficher le message de la fonction searh
    url(r'^$',views.listing, name="listing"),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name="detail"),
    
    
    
]