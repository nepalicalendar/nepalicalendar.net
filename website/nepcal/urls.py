from django.conf.urls import patterns, url

from . import views

urlpatterns = [
    url(r'^$', views.MonthlyCalendar.as_view(), name='home'),

    url(r'^(?P<year>[0-9]{4})$',
        views.MonthlyCalendar.as_view(), kwargs={'month': 1}),

    url(r'^(?P<year>\d+)/(?P<month>[0-9][0-2]?)$',
        views.MonthlyCalendar.as_view(), name='calendar'),
]
