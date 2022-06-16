from django.contrib import admin

# Register your models here.
from.models import Order, Order_item

admin.site.register(Order)
admin.site.register(Order_item)