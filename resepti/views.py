from django.http import HttpResponse
from django.shortcuts import render
from .models import Recipe, Step


def index(request):
    return HttpResponse("Hello world! You're at the index")


def detail(request, recipe_id):
    return HttpResponse(f"You're looking at recipe {recipe_id}.")


def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = set()
    for recipe in recipes:
        categories.add(recipe.category)
    context = {
        'recipes': recipes,
        'categories': categories
    }
    return render(request, 'resepti/recipe_list.html', context)
