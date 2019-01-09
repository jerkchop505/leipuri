from django import forms
from django.forms import ModelForm
from .models import Ingredient


class RecipeForm(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    category = forms.CharField(label='category', max_length=255)
    servings = forms.IntegerField(label='servings')


class RecipeIngredientForm(forms.Form):
    ingredient = forms.ModelChoiceField(Ingredient.objects.all())
    quantity = forms.DecimalField(min_value=0, decimal_places=2, label='quantity', required=False)
    weight = forms.DecimalField(min_value=0, decimal_places=2, label='weight', required=False)


class RecipeStepForm(forms.Form):
    text = forms.CharField()


class IngredientForm(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    category = forms.CharField(label='category', max_length=255)
    density = forms.DecimalField(min_value=0, decimal_places=8, label='density', required=False)
    calories_per_each = forms.IntegerField(min_value=0, label='calories by item', required=False)
    calories_per_gram = forms.IntegerField(min_value=0, label='calories by weight', required=False)

# class IngredientForm(ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = ['name', 'category', 'density', 'calories_per_each', 'calories_per_gram']
#         