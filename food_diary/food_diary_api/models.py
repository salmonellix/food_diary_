from django.db import models

from django.db import models
from django.db.models import Q


from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(default='', null=True)

    def __str__(self):
        name = str(self.first_name)
        if self.last_name:
            name += ' ' + str(self.last_name)
        return name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    calories = models.FloatField(default=0, null=True)
    proteins = models.FloatField(default=0, null=True)
    carbs = models.FloatField(default=0, null=True)
    fats = models.FloatField(default=0, null=True)

    def __str__(self):
        return self.product_name


class FoodPortion(models.Model):
    MEALS = (
        ('BREAKFAST', 'breakfast'),
        ('SNACK I', 'snack I'),
        ('LUNCH', 'lunch'),
        ('SNACK II', 'snack II'),
        ('SNACK III', 'snack III'),
        ('DINER', 'diner'),
        ('SNACK IV', 'snack IV')
    )
    meal_type = models.CharField(max_length=100, choices=MEALS)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    date = models.DateField(default='')

    def __str__(self):
        return str(self.product)
