from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RecipeForm
from .models import Recipe, Ingredient, RecipeIngredient
from .utils import get_ingredients


def index(request):
    post_list = Recipe.objects.order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html',
                  {'page': page, 'paginator': paginator})


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    context = {'form': form}
    if request.method != 'POST':
        return render(request, 'new_recipe.html', context)
    else:
        ingredients = get_ingredients(request)
        # print(ingredients)
        if not ingredients:
            form.add_error(None, "Добавьте ингредиенты")
        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            for ing_title, amount in ingredients.items():
                # print(f'{ing_title} - {amount}')
                ingredient = get_object_or_404(Ingredient, title=ing_title)
                recipe_ing = RecipeIngredient(
                    recipe=recipe, ingredient=ingredient, amount=amount
                )
                # print(recipe_ing)
                recipe_ing.save()
            # form.save_m2m()
            return redirect("index")
