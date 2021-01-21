from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.viewsets import ViewSet
from django.contrib.auth.decorators import login_required
import json

from recipes.models import Ingredient, Recipe, FavoriteRecipe, User, \
    Subscription

from .serializers import IngredientSerializer


@login_required
@api_view(['GET'])
def ingredients(request):
    query = request.GET.get('query')  # почитать теорию
    data = Ingredient.objects.filter(title__contains=query).all()
    serializer = IngredientSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)


class FavoritesView(LoginRequiredMixin, View):
    def post(self, request):
        req = json.loads(request.body)
        recipe_id = req.get('id', None)
        if recipe_id is not None:
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            obj, created = FavoriteRecipe.objects.get_or_create(
                user=request.user, recipe=recipe)
            if created:
                return JsonResponse({'success': True})
            return JsonResponse({'success': False})
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, recipe_id):
        recipe = get_object_or_404(FavoriteRecipe, recipe=recipe_id,
                                   user=request.user)
        recipe.delete()
        return JsonResponse({'success': True})


class SubscriptionView(LoginRequiredMixin, View):
    def post(self, request):
        req = json.loads(request.body)
        print(req)
        author_id = req.get('id', None)
        if author_id is not None:
            author = get_object_or_404(User, pk=author_id)
            obj, created = Subscription.objects.get_or_create(
                user=request.user, author=author)
            if created:
                return JsonResponse({'success': True})
            return JsonResponse({'success': False})
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, author_id):
        author = get_object_or_404(Subscription, author=author_id,
                                   user=request.user)
        author.delete()
        return JsonResponse({'success': True})
