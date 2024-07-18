from django.shortcuts import render, HttpResponse
from .models import CustomInfo
from django.utils import timezone
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html")

def portfolio(request):
    return render(request, "portfolio.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def valid_email(email):
    validator = EmailValidator()
    try:
        validator(email)
        return True
    except ValidationError:
        return False

def contact(request):
    if request.method == 'POST' and 'send' in request.POST:
        name = request.POST['name']
        gmail = request.POST['gmail']
        phone = request.POST['phone']
        msg = request.POST['message']
        
        if (len(name)>20 or len(name)<1):
            return HttpResponse('Your name is too long!')
        elif (len(phone)>15 or len(phone)<1):
            return HttpResponse('Your phone number is too long!')
        elif len(msg)>200 or len(msg)<1:
            return HttpResponse('The message is too long!')
        elif not valid_email(gmail) or len(gmail)<1:
            return HttpResponse('The email format is wrong!')
        else: 
            regtime = timezone.now()
            new_info = CustomInfo(name=name, gmail=gmail, phone=phone, message=msg, register_time = regtime)
            new_info.save()

    return render(request, "contact.html")

