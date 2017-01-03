from django.http import HttpResponse
from django.shortcuts import render
from .models import Cart, Service, Location

def index(request):

    location_list = Location.objects.all()
    cart_list = Cart.objects.all()
    service_list = Service.objects.all()


    context = {'location_list': location_list,
               'cart_list' : cart_list,
               'service_list' : service_list}

    return render(request, 'polls/index.html', context)

def location(request, location_id):

    current_location = ''
    cart_array = Cart.objects.order_by('-cartLocation')
    cart_list = []

    for i in cart_array:
            if str(i.cartLocation.id) == str(location_id):
                current_location = i.cartLocation
                cart_list.append(i)

    context = {'location_id': location_id,
               'current_location' : current_location,
               'cart_list' : cart_list }

    return render(request, 'polls/location.html', context)

def cart(request, location_id, cart_id):
    cart_array = Cart.objects.order_by('-cartLocation')
    cart_location = ''
    cart_obj = ''

    service_obj = Service.objects.order_by('-date_in')
    service_array = []


    for cart in cart_array:
        if str(cart.cart_id) == str(cart_id):
            cart_location = cart.cartLocation
            cart_obj = cart

    for service in service_obj:
        if str(service.cart) == str(cart_id):
            service_array.append(service)

    context = {'cart_id' : cart_id,
               'cart_obj' : cart_obj,
               'services' : service_array,
               'cart_location' : cart_location,
               'location_id': location_id}

    return render(request, 'polls/cart.html', context)


def service(request, location_id, cart_id,service_id):

    for service in Service.objects.all():
        if str(service.id) == str(service_id):
            service_obj = service


    context = {'service_id' : service_id,
               'service_obj' : service_obj
              }

    return render(request, 'polls/service.html', context)

