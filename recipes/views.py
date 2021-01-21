from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import RecipeForm
from .models import (Recipe, Ingredient, RecipeIngredient, User,
                     FavoriteRecipe, Subscription)
from .utils import get_ingredients


def index(request):
    tags = request.GET.getlist('tag')
    recipe_list = Recipe.objects.tag_filter(tags)
    paginator = Paginator(recipe_list, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html',
                  {'page': page, 'paginator': paginator})


@login_required
def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    context = {'form': form}
    if request.method != 'POST':
        return render(request, 'recipes/new_recipe.html', context)
    else:
        ingredients = get_ingredients(request)
        # print(ingredients)
        if not ingredients:
            form.add_error(None, "Добавьте ингредиенты")
        elif form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()
            for ing_title, amount in ingredients.items():
                # print(f'{ing_title} - {amount}')
                ingredient = get_object_or_404(Ingredient, title=ing_title)
                recipe_ing = RecipeIngredient(
                    recipe=recipe, ingredient=ingredient, amount=amount
                )
                # print(recipe_ing)
                recipe_ing.save()
            return redirect("index")


def profile(request, username):
    tags = request.GET.getlist('tag')
    author = get_object_or_404(User, username=username)
    post_list = Recipe.objects.tag_filter(tags).filter(author=author)
    paginator = Paginator(post_list, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/profile.html',
                  {'author': author, 'page': page, 'paginator': paginator})
    # if request.user.is_authenticated:
    #     is_follower = Follow.objects.is_following(request.user, author)
    #     return render(request, 'profile.html',
    #                   {'author': author, 'page': page, 'paginator': paginator,
    #                    'is_follower': is_follower})
    # else:
    #     return render(request, 'profile.html',
    #                   {'author': author, 'page': page, 'paginator': paginator})


def recipe_view(request, username, recipe_id):
    author = get_object_or_404(User, username=username)
    recipe = get_object_or_404(author.author_recipes, pk=recipe_id)
    # form = CommentForm()
    return render(request, 'recipes/single_page.html',
                  {'author': author, 'recipe': recipe})


@login_required
def favorite_recipe(request):
    tags = request.GET.getlist('tag')
    favorite_list = FavoriteRecipe.objects.favorite_recipe(request.user, tags)
    paginator = Paginator(favorite_list, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/favorite.html',
                  {'page': page, 'paginator': paginator})


@login_required
def subscriptions_index(request):
    subscriptions_list = Subscription.objects.subscriptions(user=request.user)
    paginator = Paginator(subscriptions_list, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'recipes/subscription.html',
                  {'page': page, 'paginator': paginator})
