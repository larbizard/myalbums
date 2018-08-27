from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^login/$', views.login_view),
    url(r'^register/$', views.register_view),
    url(r'^logout/$', views.logout_view),
]

# https://www.youtube.com/watch?v=M5ytu6yzod0
# Try Django 1.9 - 19 of 38 - URL Links & Get Absolute URL
