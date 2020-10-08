from django.conf import settings
from django import template

from paginator.paginators import paginate

register = template.Library()

PAGINATOR_THEME = getattr(settings, "PAGINATOR_THEME", "bootstrap4")
BASIC_THEME = 'paginator/{}/paginator.html'.format(PAGINATOR_THEME)
BOOTSTRAP_THEME = 'paginator/bootstrap/paginator.html'
BOOTSTRAP4_THEME = 'paginator/bootstrap4/paginator.html'


@register.inclusion_tag(BOOTSTRAP_THEME, takes_context=True)
def bootstrap_paginator(context):
    return paginate(context)


@register.inclusion_tag(BOOTSTRAP4_THEME, takes_context=True)
def bootstrap4_paginator(context):
    return paginate(context)


@register.inclusion_tag(BASIC_THEME, takes_context=True)
def paginator(context):
    return paginate(context)
