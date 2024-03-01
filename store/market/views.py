from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_list_or_404
from .models import *
from .forms import *
from .serializers import *

from django.views import View
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework.response import Response

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
    
class ContactUsView(View):

    def get(self,request):
        form = ContactUsForm()
        context = {'form':form}
        return render(request, 'contactus.html', context=context)

    def post(self,request):
        form = ContactUsForm(request.post)
        if form.is_valid():
            ...
        else:
            return render(request, 'contactus.html', {'form':form})
        
class CartAddView(View):
    def get(self, requset, pk):
        obj = get_list_or_404(models.Product, pk=pk)
        if 'cart' in requset.session:
            cart = requset.session['cart']
        else:
            cart = {}
        id = str(pk)
        if id in cart:
            cart+=1
        else:
            cart=1
        requset.session['cart'] = cart
        return redirect('market:product_list')
class CommentView(View):
    ...

class ProductListAPIView(APIView):
    """
    Hello
    """
    def get(self, request):
        product = Product.objects.filter(count__lte = 5)
        serializer = ProductSerializer(product, many=True)
        return Response(data=serializer.data)