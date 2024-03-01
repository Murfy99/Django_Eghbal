from django.urls import path, include
from market import views
from .views import *

app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),
    path('cart/add/<int:uuid>', views.CartAddView.as_view(), name='cart_add'),
    path('new', views.ProductListAPIView.as_view(), name='product_list2'),
]
