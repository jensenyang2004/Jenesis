from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.

def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    return render(request, "contact.html")

