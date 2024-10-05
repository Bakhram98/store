from django.shortcuts import render, HttpResponse


def index(request):
    context = {
        'title': 'Наше новое название!',
        'is_promotion': True,
    }
    return render(request, 'products/products.html', context)


def products1(request):
    return render(request, 'products/products.html')

# Create your views here.
