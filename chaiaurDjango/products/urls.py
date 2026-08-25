from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_cart,
    cart,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    checkout,
)


urlpatterns = [
    path('', product_list, name='product_list'),

    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),

    path('cart/', cart, name='cart'),

    path('checkout/', checkout, name='checkout'),

    path('cart/increase/<int:id>/', increase_quantity, name='increase_quantity'),

    path('cart/decrease/<int:id>/', decrease_quantity, name='decrease_quantity'),

    path('cart/remove/<int:id>/', remove_from_cart, name='remove_from_cart'),

    path('<int:id>/', product_detail, name='product_detail'),
]
from django.urls import path
from .views import (
    product_list,
    product_detail,
    add_to_cart,
    cart,
    increase_quantity,
    decrease_quantity,
    remove_from_cart,
    checkout,
    payment,
)


urlpatterns = [
    path('', product_list, name='product_list'),

    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),

    path('cart/', cart, name='cart'),

    path('checkout/', checkout, name='checkout'),

    path('payment/', payment, name='payment'),

    path('cart/increase/<int:id>/', increase_quantity, name='increase_quantity'),

    path('cart/decrease/<int:id>/', decrease_quantity, name='decrease_quantity'),

    path('cart/remove/<int:id>/', remove_from_cart, name='remove_from_cart'),

    path('<int:id>/', product_detail, name='product_detail'),
]