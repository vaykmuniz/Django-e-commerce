from django.db import models

# Create your models here.
class Customer(models.Model):
    login       = models.CharField(max_length=50)
    password    = models.CharField(max_length=32) 
