from django import template
from django.db.models import Count
from blog.models import Category, Tag

register = template.Library()


@register.inclusion_tag('blog/menu.html')
def show_menu():
    categories = Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    return {"categories": categories}


@register.inclusion_tag('blog/footer_menu.html')
def show_menu_footer():
    categories = Category.objects.annotate(cnt=Count('post')).filter(cnt__gt=0)
    tag = Tag.objects.all()
    context = {
        'categories': categories,
        'tag': tag,
    }

    return (context)