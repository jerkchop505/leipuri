from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    # grams per centimeter cubed
    density = models.DecimalField(
        decimal_places=8,
        max_digits=12,
        null=True
    )
    calories_per_gram = models.IntegerField(default=0)
    calories_per_each = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Step(models.Model):
    number = models.IntegerField()
    text = models.TextField(max_length=255)
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text


class IngredAmount(models.Model):
    # 1 weight unit is 1 gram
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        null=True
    )
    quantity = models.DecimalField(
        decimal_places=2,
        max_digits=7,
        null=True
    )
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if (self.weight is None):
            ingred = str(self.quantity) + " "
        else:
            ingred = str(self.weight) + "g "
        return ingred + self.ingredient.name


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    servings = models.IntegerField()

    def __str__(self):
        return self.name
