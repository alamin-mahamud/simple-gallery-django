from django import template

register = template.Library()

@register.filter
def addstring(s1, s2):
    return str(s1) + str(s2)