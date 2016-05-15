from nepalicalendar import NepDate, NepCal, values


def inject_date_params(request):
    """
    Injects a 'today' variable in template context
    """
    return {
        'today': NepDate.today(),
        'nepcal_values': values,
    }
