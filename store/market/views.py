from django.shortcuts import render

# Create your views here.
def product_list(request):
    name = "ali"
    contex = {
        'username': name
    }
    return render(request, 'product_list.html', context=contex)