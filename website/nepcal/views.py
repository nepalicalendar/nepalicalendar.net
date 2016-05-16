from django.shortcuts import render, Http404
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
    # Make sure month and year are within limits
    if year < 2000 or (year==2000 and month==1):
        raise Http404

    if year > 2080:
        raise Http404

    calendar = NepCal.monthdatescalendar(year, month)
    firstdate = NepDate(year, month, 1)

    prevmonth = firstdate
    nextmonth = firstdate
    try:
        prevmonth = NepDate(year - 1 if month == 1 else year,
                            12 if month == 1 else month - 1, 1)
    except:
        pass  # Do nothing on overflow

    try:
        nextmonth = NepDate(year+1 if month==12 else year,
                1 if month==12 else month+1, 1)
    except:
        pass

    context = {
        "title": "Monthly Calendar",
        "firstdate": firstdate,
        "prevmonth": prevmonth,
        "nextmonth": nextmonth,
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
