from django.contrib import admin

from .models import Buyer, Order

# Register your models here.

admin.site.register(Buyer)
admin.site.register(Order)