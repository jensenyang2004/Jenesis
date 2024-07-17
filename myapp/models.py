from django.db import models

# Create your models here.
# object relation mapping

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    
class CustomsInfo(models.Model):
    name = models.CharField(max_length=20)
    register_time = models.DateField()
    gmail = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=200)