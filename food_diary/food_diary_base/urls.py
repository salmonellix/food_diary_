from django.urls import path
from django.urls import include, path
from . import views
from .views import HomeView



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('diary/', views.UserDatesListView.as_view(), name='diary'),
    path('day/<rid>1[0-9]+', views.UserDayListView.as_view(), name='day'),
    # path('product-delete/<int:id>/<int:rid>/', views.productDelete, name="product-delete"),
    # path('add-product/', views.add_product, name='add_product'),
    # path('login/', views.login_view, name='log_in'),
    # path('product-create/', views.productCreate, name='product-create'),
    path('accounts/', include('django.contrib.auth.urls')),

]