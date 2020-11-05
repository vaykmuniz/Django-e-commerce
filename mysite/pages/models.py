from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Customer(models.Model):
    login       = models.CharField(max_length=50)
    password    = models.CharField(max_length=32) 