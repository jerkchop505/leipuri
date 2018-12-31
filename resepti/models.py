from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    itype = models.CharField(max_length=255)
    # 1 weight unit is 1 milligram
    weight = models.IntegerField(null=True)
    # 1 volume unit is 1 microliter
    volume = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    number = models.IntegerField()
    text = models.CharField(max_length=255)
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    servings = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
