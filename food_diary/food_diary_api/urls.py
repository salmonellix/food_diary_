from django.urls import path
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'users', views.ProfileViewSet)
router.register(r'food_portions', views.FoodPortionViewSet)

urlpatterns = [
    path('', include(router.urls))
]

