from django import template
from django.db.models import Count
from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/category_list.html')
def get_category_post ():
    categories = (
        Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    )
    context = {
        'categories': categories,
    }
    return (context)


@register.inclusion_tag('blog/category_list_one.html')
def get_category_post_one():
    categories = (
        Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    )


    context = {
        'categories': categories,

    }
    return (context)


@register.inclusion_tag('blog/widget_post.html')
def widget_post():
    posts = (
        Post.objects.all()
    )

    context = {
        'posts': posts,

    }
    return (context)