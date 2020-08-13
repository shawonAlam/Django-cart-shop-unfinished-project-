from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

def index(request):
    fruitProduct = Product.objects.all()
    # return HttpResponse("Helo world")
    return render(request, 'index.html',
                  {'fruit': fruitProduct})

def new(request):
    return HttpResponse("new pproducts")


