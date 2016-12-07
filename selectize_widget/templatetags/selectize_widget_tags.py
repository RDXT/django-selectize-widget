# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def selectize_widget_css():
    css_template = u'<link rel="stylesheet" href="{}" type="text/css" charset="utf-8">'
    css = css_template.format(settings.SELECTIZE_WIDGET_CSS)
    return mark_safe(css)


@register.simple_tag
def selectize_widget_js():
    js_template = u'<script src="{}" type="text/javascript" charset="utf-8"></script>'
    js = js_template.format(settings.SELECTIZE_WIDGET_JS)
    js += js_template.format(staticfiles_storage.url('selectize_widget/js/selectize_init.js'))
    return mark_safe(js)
