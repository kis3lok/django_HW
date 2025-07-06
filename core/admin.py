from django.contrib import admin
from .models import Master, Order, Review, Service

# Register your models here.
admin.site.register(Master)
admin.site.register(Order)
admin.site.register(Review)
admin.site.register(Service)
