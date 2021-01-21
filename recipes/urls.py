from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_recipe, name='new_recipe'),
    path('favorite/', views.favorite_recipe, name='favorite_recipe'),
    path('subscription/', views.subscriptions_index,
         name='subscriptions_index'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/<int:recipe_id>/', views.recipe_view, name='recipe_view'),
]
