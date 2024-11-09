from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    news = News.objects.all()
    context = {
        'title': 'Новости',
        'news': news,
    }
    return render(request, 'products/main1.html', context)


def products1(request):
    return render(request, 'products/products.html')

# Create your views here.
