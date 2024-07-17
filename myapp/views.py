from django.shortcuts import render, HttpResponse
from .models import CustomsInfo
from django.utils import timezone
from django.http import HttpResponse
from django.core.validators import validate_email

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
    if request.method == 'POST':
        name = request.POST['name']
        gmail = request.POST['gmail']
        phone = request.POST['phone']
        msg = request.POST['message']
        
        if len(name)>20:
            return HttpResponse('Your name is too long!')
        elif len(phone)>15:
            return HttpResponse('Your phone number is too long!')
        elif len(msg)>200:
            return HttpResponse('The message is too long!')
        elif not validate_email(gmail):
            return HttpResponse('The message is too long!')
        else: 
            regtime = timezone.now()
            new_info = CustomsInfo(name=name, gmail=gmail, phone=phone, message=msg, register_time = regtime)
            new_info.save()
        
    return render(request, "contact.html")

