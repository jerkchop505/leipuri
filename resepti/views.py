from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Recipe, Step, IngredAmount
from .forms import RecipeForm, RecipeIngredientForm, RecipeStepForm


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
        return HttpResponseRedirect(reverse('recipe_edit', args=(r.id,)))

    context = {
        'form': form
    }
    return render(request, 'resepti/create_recipe.html', context)


def recipe_edit(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    ingred_amounts = IngredAmount.objects.filter(recipe__id=recipe_id)
    steps = Step.objects.filter(recipe__id=recipe_id)
    i_form = RecipeIngredientForm(request.POST)
    s_form = RecipeStepForm(request.POST)
    context = {
        'recipe': recipe,
        'ingred_amounts': ingred_amounts,
        'steps': steps,
        'i_form': i_form,
        "s_form": s_form
    }
    if request.method == 'POST':
        if i_form.is_valid():
            fd = i_form.cleaned_data
            amt = IngredAmount(
                quantity=fd['quantity'],
                weight=fd['weight'],
                recipe=recipe,
                ingredient=fd['ingredient']
            )
            amt.save()
        if s_form.is_valid():
            fd = s_form.cleaned_data
            high_num = 0 if len(steps) == 0 else steps.order_by('-number')[0].number
            step = Step(
                number=high_num + 1,
                text=fd['text'],
                recipe=recipe
            )
            step.save()
        return HttpResponseRedirect(reverse('recipe_edit', args=(recipe.id,)))
    return render(request, 'resepti/add_elements_to_recipe.html', context)
