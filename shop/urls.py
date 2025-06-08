from django.urls import path
from .views import home, car_list, cart, login_view, add_to_cart, clear_cart, checkout, order_success

urlpatterns = [
    path('', home, name='home'),
    path('cars/', car_list, name='car_list'),
    path('cart/', cart, name='cart'),
    path('login/', login_view, name='login'),
    path('add_to_cart/<int:car_id>/', add_to_cart, name='add_to_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_success/', order_success, name='order_success'),
]
