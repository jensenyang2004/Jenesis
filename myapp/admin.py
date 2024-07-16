from django.contrib import admin
from .models import TodoItem

# Register your models here.
# if an admin login, the admin can check these registered database models 
admin.site.register(TodoItem)