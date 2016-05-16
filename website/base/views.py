from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpRequest
from django.views.generic import TemplateView

from nepalicalendar import NepDate

from nepcal.views import MonthlyCalendarBaseView

class HomeView(TemplateView, MonthlyCalendarBaseView):
    """
    Home page of nepalicalendar
    """
    template_name = 'base/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        today = NepDate.today()
        self.set_date(today.year, today.month)
        context.update(self.get_context())
        context['title'] = "Nepali Calendar : Official Nepali Calendar with Tithis (Nepali Patro) and Observances."
        return context
