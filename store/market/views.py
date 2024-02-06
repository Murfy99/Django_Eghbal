from django.shortcuts import render
from .models import *
from django.views import View
# # Create your views here.
# def product_list(request):
#     objs = Product.objects.all()
#     contex = {
#         'products': objs
#     }
#     return render(request, 'product_list.html', context=contex)

class ProductListView(View):
    def get (self, request):
        objs = Product.objects.all()
        context = {
            'products': objs
        }
        return render(request, 'product_list.html', context=context) 