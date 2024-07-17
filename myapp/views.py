from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your views here.
def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def guard(request):
    return render(request, "guard.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def contact(request):
    return render(request, "contact.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})