from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_recipe, name='new_recipe'),
    path('favorite/', views.favorite_recipe, name='favorite_recipe'),
    path('subscription/', views.subscriptions_index,
         name='subscription'),
    path('shopping/', views.shopping_list, name='shopping_list'),
    path('shopping/<int:recipe_id>/', views.delete_purchase,
         name='delete_purchase'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('<username>/<int:recipe_id>/edit/', views.recipe_edit,
         name='recipe_edit'),
    path('<username>/<int:recipe_id>/delete/', views.recipe_delete,
         name='recipe_delete')
]
