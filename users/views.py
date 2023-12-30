from django.shortcuts import render

from django.http import HttpResponse

# create your views

def home(request):
    return render(request , 'users/main.html')

def products(request):
    return render(request , 'users/products.html')

def customers(request):
    return render(request , 'users/customers.html')
# Create your views here.
