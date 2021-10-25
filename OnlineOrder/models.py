from django.db import models
from datetime import datetime

# Create your models here.

class OnlineContact(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

class OnlineOrders(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    products_selection = models.CharField(max_length=500)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    
