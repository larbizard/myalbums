from django.conf.urls import url

from . import views

app_name = 'albums'
urlpatterns = [
    url(r'^$', views.overview, name="overview"),
    url(r'^createAlbum/$', views.createAlbum, name="createAlbum"),
    url(r'^(?P<id>\d+)/$', views.detailAlbum, name="detailAlbum"),
    url(r'^albumScore/$', views.albumScore, name="albumScore"),
    url(r'^profil/$', views.profil, name="profil"),
]