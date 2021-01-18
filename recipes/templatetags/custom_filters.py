from django import template
from recipes.models import FavoriteRecipe, Tag

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def is_favorite(recipe, user):
    return FavoriteRecipe.objects.filter(recipe=recipe, user=user).exists()


@register.filter
def all_tags(value):
    return Tag.objects.all()


@register.filter
def get_active_tags(value):
    return value.getlist('tag')


@register.filter
def change_tag_link(request, tag):
    copy = request.GET.copy()
    tag_link = copy.getlist('tag')
    if tag.slug in tag_link:
        tag_link.remove(tag.slug)
        copy.setlist('tag', tag_link)
    else:
        copy.appendlist('tag', tag.slug)
    return copy.urlencode()
