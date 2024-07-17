from django.urls import path
from . import views 

urlpatterns = [
    #a url patterns
    path("index/", views.index, name="index"), 
    path('index/about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name = 'service')
]
