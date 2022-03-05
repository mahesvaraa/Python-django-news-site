from django import template

from news.models import Category
from django.db.models import Count
register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(cnt=Count('news'))


@register.inclusion_tag('inc/_sidebar.html')
def show_categories():
    #categories = get_categories()
    categories = Category.objects.annotate(cnt=Count('news'))
    print(categories[0].cnt)
    return {'categories': categories}
