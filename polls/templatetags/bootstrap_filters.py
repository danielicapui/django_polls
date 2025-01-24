from django import template
#https://github.com/mlocati/gettext-iconv-windows/releases/tag/v0.23-v1.17
register= template.Library()
@register.filter(name='add_class')
def add_class(value,arg):
    return value.as_widget(attrs={'class':arg})