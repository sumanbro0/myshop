from django.contrib import admin

from .models import Contact, OrderUpdate, Orders, product

# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
