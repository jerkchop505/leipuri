from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe, Step, IngredAmount
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
    categories = ['appetizer', 'entree', 'side', 'bread', 'dessert']

    form = RecipeForm(request.POST)
    i_form = RecipeIForm(request.POST)
    if form.is_valid() and i_form.is_valid():
        fd = form.cleaned_data
        fdi = i_form.cleaned_data
        print(fdi)
        r = Recipe(name=fd['name'], category=fd['category'], servings=fd['servings'])
        r.save()
        return HttpResponseRedirect(reverse('recipe_detail', args=(r.id,)))

    context = {
        'categories': categories,
        'form': form,
        'i_form': i_form
    }
    return render(request, 'resepti/create_recipe.html', context)
