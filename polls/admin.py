from django.contrib import admin

from .models import Cart, Service, Location, Spares

admin.site.register(Location)
admin.site.register(Cart)
admin.site.register(Service)
admin.site.register(Spares)
