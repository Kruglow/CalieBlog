from django import template
from django.db.models import Count
from blog.models import *

register = template.Library()

@register.inclusion_tag('blog/aside_menu.html')
def get_aside_menu ():
    categories = (
        Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    )
    context = {
        'categories': categories,
    }
    return (context)