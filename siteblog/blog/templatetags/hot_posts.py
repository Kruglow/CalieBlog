from django import template
from django.db.models import Count
from blog.models import *

register = template.Library()

@register.inclusion_tag('blog/hot_posts.html')
def get_hot_posts(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts':posts}