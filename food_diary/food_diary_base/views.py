from django.shortcuts import render
from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from food_diary_api.models import Meal, Profile, Product, Day
#
# from food_diary_api.serializers import ProductSerializer


def home(request):

    return render(request, 'index.html')

# def diary(request):
#     days = Day.objects.all()
#
#     context = {'days': days}
#     return render(request, 'diary.html', context)
#
#
# def day(request, rid):
#     day = Day.objects.filter(id= rid)
#     meals = Meal.objects.filter(day = day[0])
#     kcals = 0
#     for meal in meals:
#          prods = meal.products.all()
#          for prod in prods:
#              kcals += prod.count_kcal()
#
#     context = {
#         'day': day,
#         'meals': meals,
#         'kcals': kcals
#     }
#
#     return render(request, 'day.html', context)
#
# def add_product(request):
#
#     return render(request, 'add_product.html')
#
#
# def log_in(request):
#
#     return render(request, 'log_in.html')
#
# @api_view(['DELETE', 'GET'])
# def productDelete(request, id,rid):
#     meal = Meal.objects.get(id=id)
#     product = Product.objects.get(id=rid)
#     meal.products.remove(product)
#     day(request, meal.day.id)
#     return day(request, meal.day.id)
#
#
# @api_view(['POST'])
# def productCreate(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
