from django import template
from django.db.models import Count
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/aside.html')
def get_aside():
    categories = (
        Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    )
    post = (
        Post.objects.order_by('-views')[:5]
    )
    context = {
        'categories': categories,
        'post':post,
    }
    return (context)