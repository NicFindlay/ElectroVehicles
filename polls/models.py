from django.db import models


class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class Cart(models.Model):
    cart_id = models.IntegerField(blank=True, default=1)
    serial_number = models.IntegerField(null=True)
    department = models.CharField(max_length=200, null=True)
    cartLocation = models.ForeignKey(Location, blank=True, default=1)
    running_hours = models.IntegerField(blank=True, null=True)
    #cart_pic_one = models.ImageField(blank=True, null=True)
    #cart_pic_two = models.ImageField(blank=True, null=True)
    #scart_pic_three = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.cart_id)

class Service(models.Model):
    cart = models.ForeignKey(Cart, blank=True, default=1)
    technician = models.TextField(blank=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)
    serviced = models.BooleanField(blank=False, null=False, default=False)
    breakdown = models.BooleanField(blank=False, null=False, default=False)
    accident = models.BooleanField(blank=False, null=False, default=False)
    battery_percentage = models.IntegerField(null=True)
    problem = models.TextField(blank=True)
    repaired_replaced = models.TextField(blank=True)
    concerns = models.TextField(blank=True)
    parts_ordered = models.TextField(blank=True)



    def __unicode__(self):
        return str(self.cart.cart_id)




