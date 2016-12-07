# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.conf import settings as base_settings


class SelectizeWidgetConfig(AppConfig):
    name = 'selectize_widget'


class Settings(object):
    SELECTIZE_WIDGET_JS = '//cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/js/standalone/selectize.min.js'
    SELECTIZE_WIDGET_CSS = '//cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/css/selectize.bootstrap3.min.css'

    def __getattribute__(self, name):
        if hasattr(base_settings, name):
            return getattr(base_settings, name)
        return object.__getattribute__(self, name)


settings = Settings()
