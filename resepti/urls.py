"""leipuri URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('recipe_list', views.recipe_list, name="recipe_list"),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name="recipe_detail"),
    path('recipe_create', views.recipe_create, name="recipe_create"),
    path('recipe/<int:recipe_id>/ingredients', views.recipe_edit, name="recipe_edit"),
    path('ingredient_create', views.ingredient_create, name="ingredient_create"),
    path('ingredient_list', views.ingredient_list, name="ingredient_list"),
    path('ingredient/<int:ingredient_id>/', views.ingredient_edit, name="ingredient_edit")
]
