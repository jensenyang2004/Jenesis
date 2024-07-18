from django.db import models
# Create your models here.
# object relation mapping

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class CustomInfo(models.Model):
    name = models.CharField(max_length=20)
    register_time = models.DateTimeField()
    gmail = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=200)
    display = models.BooleanField(default=False)

class MemberInfo(models.Model):
    name = models.CharField(max_length=20)
    register_date = models.DateField()
    gmail = models.EmailField()
    phone = models.CharField(max_length=15)
    igAddr = models.CharField(max_length=30)
    fbAddr = models.CharField(max_length=30)
    gitHubAddr = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    photo = models.CharField(max_length=50)
    display = models.BooleanField(default=True)
    
class ServiceInfo(models.Model):
    serviceName = models.CharField(max_length=20)
    serviceDescription = models.CharField(max_length=200)
    serviceImage = models.CharField(max_length=20)
    exampleGitHubLink = models.CharField(max_length=30)
    exampleDescription = models.CharField(max_length=200) 
    exampleContributor = models.CharField(max_length=20)
    exampleStartTime =  models.DateField()
    exampleEndTime = models.DateField()
    exampleImage =  models.CharField(max_length=20)
    display = models.BooleanField(default=True)

    