from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Recipe, Step


def index(request):
    return HttpResponse("Hello world! You're at the index")


def detail(request, recipe_id):
    return HttpResponse(f"You're looking at recipe {recipe_id}.")


def recipe_list(request):
    recipes = Recipe.objects.all()
    steps = Step.objects.filter(recipe__name="spaghetti aglio e olio")
    template = loader.get_template('resepti/index.html')
    context = {
        'recipes': recipes,
        'steps': steps
    }
    return HttpResponse(template.render(context, request))
