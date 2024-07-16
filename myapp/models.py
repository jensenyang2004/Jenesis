from django.db import models

# Create your models here.
# object relation mapping

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)