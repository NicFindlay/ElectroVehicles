from django.http import HttpResponse
from django.shortcuts import render
from .models import Cart, Service, Location
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import datetime


def index(request):
    location_list = Location.objects.all()
    cart_list = Cart.objects.all()
    service_list = Service.objects.all()
    user_flag = False

    # Login functionality
    if ('username' in request.POST) and request.POST['username'].strip():
        username = request.POST['username']
        if ('password' in request.POST) and request.POST['password'].strip():
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/home", request.path)

    context = {'location_list': location_list,
               'cart_list' : cart_list,
               'service_list' : service_list,
               'user_flag' : user_flag}

    return render(request, 'polls/index.html', context)

@login_required(login_url='/')
def home(request):

    location_list = Location.objects.all()
    cart_list = Cart.objects.all()
    service_list = Service.objects.all()
    monthly_service = []
    today = datetime.date.today()
    month_ago = datetime.date.today() + datetime.timedelta(-25)

    overdue_service = []


    # for service in service_list:
    #     if (service.date_out.month == today.month):
    #         monthly_service.append(service)
    #
    # for service in monthly_service:
    #     if (service.date_out < month_ago):
    #         overdue_service.append(service)


    context = {'location_list': location_list,
               'cart_list' : cart_list,
               'service_list' : service_list,
               'monthly_service' : monthly_service,
               'overdue_service' : overdue_service}

    return render(request, 'polls/home.html', context)

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

def stats(request, location_id):

    current_location = ''
    cart_array = Cart.objects.all()
    cart_list = []
    service_obj = Service.objects.order_by('cart')
    service_array = []


    for i in cart_array:
        if str(i.cartLocation.id) == str(location_id):
            current_location = i.cartLocation
            cart_list.append(i)

    cart_length = len(cart_list)

    for service in service_obj:
        if str(service.cart) in str(cart_list):
            service_array.append(service)

    service_length = len(service_array)

    context = {'location_id': location_id,
               'current_location': current_location,
               'cart_list': cart_list,
               'cart_length' : cart_length,
               'service_array' : service_array,
               'service_length' : service_length}

    return render(request, 'polls/stats.html', context)

def spares(request, location_id):

    current_location = ''
    cart_array = Cart.objects.all()
    cart_list = []
    service_obj = Service.objects.all()
    service_array = []


    for i in cart_array:
        if str(i.cartLocation.id) == str(location_id):
            current_location = i.cartLocation
            cart_list.append(i)


    context = {'location_id': location_id,
               'current_location': current_location,
               'cart_list': cart_list}

    return render(request, 'polls/spares.html', context)

def batteries(request, location_id):

    current_location = ''
    cart_array = Cart.objects.all()
    cart_list = []
    service_obj = Service.objects.all()
    service_array = []


    for i in cart_array:
        if str(i.cartLocation.id) == str(location_id):
            current_location = i.cartLocation
            cart_list.append(i)



    context = {'location_id': location_id,
               'current_location': current_location,
               'cart_list': cart_list}

    return render(request, 'polls/batteries.html', context)

def tyres(request, location_id):

    current_location = ''
    cart_array = Cart.objects.all()
    cart_list = []
    service_obj = Service.objects.all()
    service_array = []


    for i in cart_array:
        if str(i.cartLocation.id) == str(location_id):
            current_location = i.cartLocation
            cart_list.append(i)



    context = {'location_id': location_id,
               'current_location': current_location,
               'cart_list': cart_list}

    return render(request, 'polls/tyres.html', context)

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

def history( request, location_id, cart_id):
    cart_array = Cart.objects.order_by('-cartLocation')
    cart_location = ''
    cart_obj = ''

    for cart in cart_array:
        if str(cart.cart_id) == str(cart_id):
            cart_location = cart.cartLocation
            cart_obj = cart

    service_obj = Service.objects.order_by('-date_in')
    service_array = []

    for service in service_obj:
        if str(service.cart) == str(cart_id):
            service_array.append(service)

    context = {'service_array' : service_array,
               'cart_obj' : cart_obj}

    return render(request, 'polls/history.html', context)

def service(request, location_id, cart_id,service_id):

    for service in Service.objects.all():
        if str(service.id) == str(service_id):
            service_obj = service


    context = {'service_id' : service_id,
               'service_obj' : service_obj
              }

    return render(request, 'polls/service.html', context)

