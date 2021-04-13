from django.shortcuts import render
from django.shortcuts import render
from rest_framework import filters
from rest_framework import filters, mixins
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework import generics


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('first_name')
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('product_name')
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product_name']

    # delete item only when it is not in use
    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        rid = product.id
        products = Product.objects.filter(id=rid)
        if not products:
            product.delete()
            return Response('Item succsesfully delete!')
        else:
            return Response('Cant delete!')

class FoodPortionViewSet(viewsets.ModelViewSet):
    queryset = FoodPortion.objects.all().order_by('date')
    serializer_class = FoodPortionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['product', 'date', 'profile']


class StudentGradesListView(APIView):

    def get(self, request, *args, **kwargs):
        student: User = User.objects.get(studentID=kwargs['studentID'])
        grades = Grade.objects.filter(student=student)
        return Response(ExamGradesSerializer(grades, many=True).data)