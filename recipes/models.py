from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# verbose_name, related_name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='ingredient name')
    unit = models.CharField(max_length=64,
                            verbose_name='ingredient unit')

    def __str__(self):
        return f'{self.pk} - {self.name} - {self.unit}'


class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_recipes')
    title = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='recipe/', blank=True,
    #                           null=True)
    description = models.TextField(blank=True,
                                   verbose_name='recipe description')
    ingredients = models.ManyToManyField(Ingredient,
                                         through='RecipeIngredient') # related
    # tags =
    cooking_time = models.IntegerField()
    # slug = models.SlugField(max_length=200, unique=True)
    pub_date = models.DateTimeField(verbose_name='date published',
                                    auto_now_add=True,
                                    db_index=True)

    def __str__(self):
        return f'{self.pk} - {self.title} - {self.author}'


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE) # related_name here
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    amount = models.IntegerField()
