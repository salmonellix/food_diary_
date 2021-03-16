from django.contrib import admin

from .models import Profile, Product, FoodPortion

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(FoodPortion)
