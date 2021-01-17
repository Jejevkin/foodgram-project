from django import template
from recipes.models import FavoriteRecipe

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter
def is_favorite(recipe, user):
    return FavoriteRecipe.objects.filter(recipe=recipe, user=user).exists()
