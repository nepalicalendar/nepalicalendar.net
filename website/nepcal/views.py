from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest

from nepalicalendar import NepDate, NepCal, NEPALI_MONTH_NAMES_NE


def calendar(request, year, month=1):
    """
    Show the nepali calendar of the year and month
    """
    template = loader.get_template('nepcal/calendar.html')

    month = int(month)
    year = int(year)

    calendar = NepCal.monthdatescalendar(year, month)
    firstdate = NepDate(year, month, 1)

    context = {
        "title": "Monthly Calendar",
        "firstdate": firstdate,
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
