from django.shortcuts import render
from django.core.urlresolvers import reverse
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
        context['title'] = "Nepali Calendar :  नेपाली पात्रो "
        return context


class HomeViewBase(object):

    def get_context(self):
        return {
            "breadcrumbs": [("Home", " /")]
        }


class AboutUsView(TemplateView, HomeViewBase):
    """
    About Us Page
    """
    template_name = 'base/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context.update(self.get_context())
        context['title'] = "Nepali Calendar : About Us"
        context['breadcrumbs'].append(
            ("About Us", reverse('about'))
        )
        context['breadcrumb_title'] = "About Us"
        return context
