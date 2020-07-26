from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home_view(request, *args, **kwargs):
    #obj = Product.objects.get(id=1)
    return render(request, "home.html", {})

def products_index(*args, **kwargs):
    return HttpResponse("<h1>Hello Product Index</h1>")

def products_new(*args, **kwargs):
    return HttpResponse("<h1>Hello Product Create New</h1>")

def products_show(*args, **kwargs):
    return HttpResponse("<h1>Hello Product Show</h1>")

