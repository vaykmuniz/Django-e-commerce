from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class UserOrder(models.Model):
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order       = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_added  = models.DateTimeField(auto_now=True)