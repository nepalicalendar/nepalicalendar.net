from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest

from nepalicalendar import NepDate, NepCal


def calendar(request, year, month=1):
    """
    Show the nepali calendar of the year and month
    """
    template = loader.get_template('nepcal/calendar.html')

    month = int(month)
    year = int(year)

    context = {
        "title": "Monthly Calendar",
        "year": year,
        "month": month,
        "monthlycalendar": NepCal.monthdatescalendar(year, month),
    }
    return HttpResponse(template.render(context, request))


def home(request):
    """
    Calendar home. Display the calendar of current year and day
    in nepali
    """
    today = NepDate.today()
    return calendar(request, today.year, today.month)
