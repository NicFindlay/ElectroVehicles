from django.contrib import admin

from .models import Cart, Service, Location

admin.site.register(Location)
admin.site.register(Cart)
admin.site.register(Service)
