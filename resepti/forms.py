from django import forms
from .models import Ingredient


class RecipeForm(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    category = forms.CharField(label='category', max_length=255)
    servings = forms.IntegerField()

    i_list = Ingredient.objects.all()
    choices = (("FR", "France"), ("EN", "England"))
    ingredients = forms.MultipleChoiceField(choices=choices)
