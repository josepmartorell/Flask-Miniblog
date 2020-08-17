
def format_datetime(value, format='short'):
    """Filter that transforms a datetime into a formatted str.

     The filter is to be used in JINJA2 templates.
     The possible formats are the following:
     * short: dd / mm / yyyy
     * full: mm dd yyyy

    :param datetime value: Date to be transformed.
    :param format: Format with which to display the date. Possible values: short and full.
    :return: A string with the date format.
    """

    value_str = None
    if not value:
        value_str = ''
    if format == 'short':
        value_str = value.strftime('%d/%m/%Y')
    elif format == 'full':
        value_str = value.strftime('%d of %m year %Y')
    else:
        value_str = ''
    return value_str
