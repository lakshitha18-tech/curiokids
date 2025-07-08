from django.urls import path
from . import views

urlpatterns = [
    path('activities/games/', views.games, name='games'),

    # Game URLs
    path('games/memory/', views.memory_game, name='memory_game'),
    path('games/math-puzzle/', views.math_puzzle, name='math_puzzle'),
    path('activities/games/spelling-bee/', views.spelling_bee, name='spelling_bee'),
    path('activities/games/guess-image/', views.guess_image, name='guess_image'),
    path('activities/games/color-match/', views.color_match, name='color_match'),
    path('activities/games/shape-sort/', views.shape_sort, name='shape_sort'),
]
