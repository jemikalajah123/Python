from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return self.username

class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField( max_length=500)
    completed = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class Actions(models.Model):
    project_id = models.ForeignKey(Projects,on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    note = models.CharField(max_length=500)

    def __str__(self):
        return self.project_id

