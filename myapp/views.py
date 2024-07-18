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
    if request.method == "POST":
        name = request.POST['name']
        gmail = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['message']

        print(name, gmail, phone, msg)


    return render(request, "contact.html")

