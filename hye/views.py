from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, profile


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products' : products})
    
def new(request):
    profiles = profile.objects.all()
    return render(request, 'profile.html')
