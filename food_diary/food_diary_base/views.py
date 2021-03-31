from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.shortcuts import render
from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from food_diary_api.models import Meal, Profile, Product, Day
from django.contrib.auth import authenticate, login, logout
#
# from food_diary_api.serializers import ProductSerializer
from django.views.generic import TemplateView

from food_diary_api.models import FoodPortion


def home(request):

    return render(request, 'index.html')

# @login_required
class HomeView(TemplateView):
    template_name = 'index.html'


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        return render(request, 'log_in.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.



class UserDatesListView(LoginRequiredMixin,ListView):
    model = FoodPortion
    template_name = 'diary.html'

    def get_queryset(self):
        return FoodPortion.objects.filter(profile = self.request.user.id).values('date','id').order_by('date')


class UserDayListView(LoginRequiredMixin,ListView):
    model = FoodPortion
    template_name = 'day.html'

    def get_queryset(self):
        return FoodPortion.objects.filter(profile = self.request.user.id).order_by('meal_type')


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
