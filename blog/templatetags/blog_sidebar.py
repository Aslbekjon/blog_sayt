from django import template

from blog.models import Category, Blog
from taggit.models import Tag


register = template.Library()

@register.inclusion_tag('category.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories':categories}

@register.inclusion_tag('tag.html')
def show_tags():
    tag = Tag.objects.all()
    return {'tag':tag}

@register.inclusion_tag('top_message.html')
def show_message_link():
    top_blog = Blog.objects.order_by('-views')[:6]
    return {'top_blog':top_blog}
