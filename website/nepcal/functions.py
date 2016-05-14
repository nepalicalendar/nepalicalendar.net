from nepalicalendar import NepDate


def inject_date_params(request):
    """
    Injects a 'today' variable in template context
    """
    return {
        'today': NepDate.today()
    }
