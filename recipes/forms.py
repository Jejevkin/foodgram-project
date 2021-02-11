from django.forms import (ModelForm)

from .models import Ingredient, Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'cooking_time', 'description', 'image',
                  'tags', 'ingredients')

    def clean(self):
        ing_added = False
        ing_in_db, amount = True, True
        for key in self.data.keys():

            if 'nameIngredient' in key:
                ing_added = True
                if not Ingredient.objects.filter(
                        title=self.data[key]).exists():
                    ing_in_db = False

            if 'valueIngredient' in key:
                if int(self.data[key]) <= 0:
                    amount = False

        if not amount:
            self.add_error('ingredients',
                           'Количесвто ингредиентов должно быть больше 0')

        if not ing_in_db:
            self.add_error('ingredients', 'Выберите ингредиент из списка')

        if not ing_added:
            self.add_error('ingredients',
                           'Добавьте ингредиенты к совему рецепту')
