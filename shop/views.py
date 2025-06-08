from django.shortcuts import render, redirect
from .models import Car, Order
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'shop/home.html')

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'shop/car_list.html', {'cars': cars})

def cart(request):
    orders = Order.objects.all()
    return render(request, 'shop/cart.html', {'orders': orders})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'shop/login.html')

def add_to_cart(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    order = Order(car=car, quantity=1)
    order.save()
    return redirect('cart')

def clear_cart(request):
    # Удаляем все заказы из корзины
    Order.objects.all().delete()
    return redirect('cart')


def checkout(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']

        return redirect('order_success')

    return render(request, 'checkout.html')

def order_success(request):
    return render(request, 'shop/order_success.html')