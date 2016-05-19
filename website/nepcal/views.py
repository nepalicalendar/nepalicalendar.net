from django.shortcuts import render, Http404
from django.template import loader
from django.http import HttpResponse, HttpRequest

from nepalicalendar import NepDate, NepCal, NEPALI_MONTH_NAMES_NE
from django.views.generic import TemplateView


class MonthlyCalendarBaseView(object):
    """ MonthlyCalendarBaseViewis the base view for any view showing calendar.
    It prepares the necessary information for displaying a nepali calendar
    """
    def set_date(self, year, month):
        """
        Sets the calendar to show the monthly calendar of given month and
        year. It prepares other information required to show the calendar
        """
        self.year = int(year)
        self.month = int(month)

        # Make sure month and year are within limits
        if self.year < 2000 or (self.year == 2000 and self.month == 1):
            raise Http404

        if self.year > 2080:
            raise Http404

        self.calendar = NepCal.monthdatescalendar(self.year, self.month)
        self.firstdate = NepDate(self.year, self.month, 1)

        self.prevmonth = self.firstdate
        self.nextmonth = self.firstdate
        try:
            self.prevmonth = NepDate(self.year - 1 if self.month == 1 else self.year,
                                     12 if self.month == 1 else self.month - 1, 1)
        except:
            pass  # Do nothing on overflow

        try:
            self.nextmonth = NepDate(self.year + 1 if self.month == 12 else self.year,
                                     1 if self.month == 12 else self.month + 1, 1)
        except:
            pass

    def get_context(self, **kwargs):
        """
        Returns all the required context for any template showing a
        calendar
        """
        context = {
            "firstdate": self.firstdate,
            "prevmonth": self.prevmonth,
            "nextmonth": self.nextmonth,
            "monthlycalendar": self.calendar,
        }
        return context


class MonthlyCalendar(TemplateView, MonthlyCalendarBaseView):
    """
    Show the monthly Calendar
    """
    template_name = "nepcal/calendar.html"

    def get_context_data(self, **kwargs):
        context = super(MonthlyCalendar, self).get_context_data(**kwargs)

        # Get the current year and month
        today = NepDate.today()
        if 'year' in self.kwargs:
            year = self.kwargs['year']
        else:
            year = today.year

        if 'month' in self.kwargs:
            month = self.kwargs['month']
        else:
            month = today.month

        self.set_date(year, month)

        context.update(self.get_context())
        context['title'] = "Nepali Calendar:  %s , वि.सं.  %s  - नेपाली पात्रो " % (
            self.firstdate.month_name(), self.firstdate.ne_year)
        return context
