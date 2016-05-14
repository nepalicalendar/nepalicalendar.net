from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest

from nepalicalendar import NepDate


def calendar(request, year, month):
    """
    Show the nepali calendar of the year and month
    """
    template = loader.get_template('nepcal/monthlycalendar.html')

    context = {
        "title": "Monthly Calendar",
        "year": year,
        "month": month,
    }
    return HttpResponse(template.render(context, request))


def home(request):
    """
    Calendar home. Display the calendar of current year and day
    in nepali
    """
    today = NepDate.today()
    return calendar(request, today.year, today.month)
