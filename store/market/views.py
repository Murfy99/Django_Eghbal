from django.shortcuts import render
from .models import *
# Create your views here.
def product_list(request):
    objs = Product.objects.all()
    contex = {
        'products': objs
    }
    return render(request, 'product_list.html', context=contex)