from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest
from nepalicalendar import NepCal, NepDate


def home(request):
    """
    Home page of nepalicalendar
    """
    template = loader.get_template('base/home.html')

    today = NepDate.today()
    month = today.month
    year = today.year

    calendar = NepCal.monthdatescalendar(year, month)
    firstdate = NepDate(today.year, today.month, 1)

    # We don't check overflow here.
    prevmonth = NepDate(year - 1 if month == 1 else year,
                        12 if month == 1 else month - 1, 1)

    nextmonth = NepDate(year + 1 if month == 12 else year,
                        1 if month == 12 else month + 1, 1)

    context = {
        "title": "Nepali Calendar : Official Nepali Calendar with Tithis (Nepali Patro) and Observances.",
        "firstdate": firstdate,
        "prevmonth": prevmonth,
        "nextmonth": nextmonth,
        "monthlycalendar": NepCal.monthdatescalendar(year, month),

    }
    return HttpResponse(template.render(context, request))
