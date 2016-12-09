# django-selectize-widget
Selectize widget for django form fields.

# Widgets
SelectizeWidget()
SelectizeMultipleWidget()

You can add attributes to the widget via selectize_attrs:
```
SelectizeWidget(selectize_attrs={
                    'hideSelected': True,
                    'load': 'vehicle_choices',
                    'searchField': 'text',
                    'valueField': 'value',
                    'labelField': 'text',
                    'preload': 'focus',
                    'plugins': 'remove_button, restore_on_backspace' #comma seperated string of plugins
                }
            )
```

# Static
```
{% load selectize_widget_tags %}
{% selectize_widget_css %}
{% selectize_widget_js %}
{{form.media}}
```

By default loads the following css and js:

SELECTIZE_WIDGET_JS = '//cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/js/standalone/selectize.min.js'
SELECTIZE_WIDGET_CSS = '//cdnjs.cloudflare.com/ajax/libs/selectize.js/0.12.4/css/selectize.bootstrap3.min.css'

But you can add what you want for them just by setting the path in settings.
