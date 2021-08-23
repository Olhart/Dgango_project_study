from django import template
from qa.models import *

register = template.Library()

@register.simple_tag(name='menu_list')
def menu():
    menu_dict = {
        'Main': 'home',
        'New': 'at_new',
        'Popular': 'at_pop',
        'Ask': 'form_ask'
    }
    return menu_dict