from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *
from django.views import View
from django.views.generic import ListView

# # Create your views here.
# def product_list(request):
#     objs = Product.objects.all()
#     contex = {
#         'products': objs
#     }
#     return render(request, 'product_list.html', context=contex)

# class ProductListView(View):
#     def get (self, request):
#         objs = Product.objects.all()
#         context = {
#             'products': objs
#         }
#         return render(request, 'product_list.html', context=context) 

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    
    paginate_by = 5
    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.filter(price__lte =10)