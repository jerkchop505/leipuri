from django import forms
from .models import Ingredient


class RecipeForm(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    category = forms.CharField(label='category', max_length=255)
    servings = forms.IntegerField(label='servings')


class RecipeIForm(forms.Form):
    i_list = Ingredient.objects.all()
    choices = []
    for ingredient in i_list:
        choices.append((ingredient.name[0:2], ingredient.name))
    ingredient = forms.ChoiceField(choices=choices, label='ingredient')
    quantity = forms.DecimalField(min_value=0, decimal_places=2, label='quantity')
