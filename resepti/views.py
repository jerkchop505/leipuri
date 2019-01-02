from django.shortcuts import render
from .models import Recipe, Step, Ingredient
from .forms import RecipeForm


def index(request):
    return render(request, 'resepti/index.html')


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = Ingredient.objects.filter(recipe__id=recipe_id)
    steps = Step.objects.filter(recipe__id=recipe_id)
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
        'steps': steps
    }
    return render(request, 'resepti/recipe_detail.html', context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = ['appetizer', 'entree', 'side', 'bread', 'dessert']
    context = {
        'recipes': recipes,
        'categories': categories
    }
    return render(request, 'resepti/recipe_list.html', context)


def recipe_entry(request):
    categories = ['appetizer', 'entree', 'side', 'bread', 'dessert']
    context = {
        'categories': categories
    }
    return render(request, 'resepti/entry_page.html', context)


def recipe_create(request):
    form = RecipeForm(request.POST)
    if form.isValid():
        print("yay")
