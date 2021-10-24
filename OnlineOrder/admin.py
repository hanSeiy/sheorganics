from django.contrib import admin
from .models import OnlineContact,OnlineOrders
# Register your models here.

admin.site.register(OnlineOrders)
admin.site.register(OnlineContact)
