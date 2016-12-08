# -*- coding: utf-8 -*-
import re

from django import forms


class SelectizeMixin(object):
    def __init__(self, attrs=None, selectize_attrs=None):
        # Immediate finalization, return the structure
        if selectize_attrs is None:
            selectize_attrs = {}
        if attrs is None:
            attrs = {}
        for k, v in selectize_attrs.items():
            # We set properties as underscore string
            underscore = re.sub('([A-Z]+)', r'-\1', k).lower()
            # we convert value to string (mainly for boolean values)
            attrs["selectize-%s" % underscore] = str(v)

        attrs['data-selectize'] = "selectize"
        super(SelectizeMixin, self).__init__(attrs)

    def _get_media(self):
        """
        Construct Media as a dynamic property.
        .. Note:: For more information visit
            https://docs.djangoproject.com/en/1.8/topics/forms/media/#media-as-a-dynamic-property
        """
        return forms.Media(
            js=('selectize_widget/js/selectize_init.js',),
        )

    media = property(_get_media)


class SelectizeWidget(SelectizeMixin, forms.Select):
    pass


class SelectizeMultipleWidget(SelectizeMixin, forms.SelectMultiple):
    pass
