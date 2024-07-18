from django.contrib import admin
from .models import *

# Register your models here.
# if an admin login, the admin can check these registered database models 
admin.site.register(TodoItem)
admin.site.register(CustomInfo)
admin.site.register(MemberInfo)
admin.site.register(ServiceInfo)