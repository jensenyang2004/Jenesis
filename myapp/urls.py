from django.urls import path
from . import views 

urlpatterns = [
    #a url patterns
    path("", views.home, name = "home"), 
    path("todos/", views.todos, name="Todos"), 
    path("index/", views.index, name="index"), 
    path('guard/', views.guard, name='guard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service')
]
