from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'products/products.html')


def products1(request):
    return render(request, 'products/products.html')

# Create your views here.
