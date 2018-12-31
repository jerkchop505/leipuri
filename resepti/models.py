from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=150)
    servings = models.IntegerField()
    ingredients = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    steps = models.ForeignKey('Step', on_delete=models.CASCADE)


class Ingredient(models.Model):
    name = models.CharField(max_length=150)
    itype = models.CharField(max_length=150)


class Step(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=255)
