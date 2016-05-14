from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpRequest

def home(request):
    """
    Home page of nepalicalendar
    """
    template = loader.get_template('base/home.html')

    context = {
        "title": "Nepali Calendar : Official Nepali Calendar with Tithis (Nepali Patro) and Observances.",
    }
    return HttpResponse(template.render(context, request))
