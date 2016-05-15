from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<year>[0-9]{4})$', views.calendar),
    url(r'^(?P<year>\d+)/(?P<month>[0-9][0-2]?)$', views.calendar, name='calendar'),
]
