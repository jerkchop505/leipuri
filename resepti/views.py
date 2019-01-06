from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe, Step, IngredAmount, Ingredient
from .forms import RecipeForm, RecipeIForm


def index(request):
    return render(request, 'resepti/index.html')


def detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingredients = IngredAmount.objects.filter(recipe__id=recipe_id)
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
    form = RecipeForm(request.POST)
    if form.is_valid():
        fd = form.cleaned_data
        r = Recipe(name=fd['name'], category=fd['category'], servings=fd['servings'])
        r.save()
        return HttpResponseRedirect(reverse('ingredient_entry', args=(r.id,)))

    context = {
        'form': form
    }
    return render(request, 'resepti/create_recipe.html', context)


def ingredient_entry(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingred_amounts = IngredAmount.objects.filter(recipe__id=recipe_id)
    form = RecipeIForm(request.POST)
    context = {
        'recipe': recipe,
        'ingred_amounts': ingred_amounts,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'resepti/add_ingredients_to_recipe.html', context)
    if request.method == 'POST':
        if form.is_valid():
            fd = form.cleaned_data
            i = IngredAmount(
                quantity=fd['quantity'],
                weight=fd['weight'],
                recipe=recipe,
                ingredient=fd['ingredient']
            )
            i.save()
            return HttpResponseRedirect(reverse('ingredient_entry', args=(recipe.id,)))
