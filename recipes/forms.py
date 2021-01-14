from django.forms import (ModelForm, ModelMultipleChoiceField,
                          CheckboxSelectMultiple)

from .models import Recipe, Tag


class RecipeForm(ModelForm):
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                    widget=CheckboxSelectMultiple(
                                        attrs={'class': 'tags__checkbox'}),
                                    required=False
                                    )

    class Meta:
        model = Recipe
        fields = ('title', 'cooking_time', 'description', 'image',
                  'tags', 'ingredients')