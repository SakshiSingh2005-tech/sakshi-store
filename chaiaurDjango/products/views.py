from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order


def product_list(request):
    category = request.GET.get('category')

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    categories = Product.objects.values_list(
        'category', flat=True
    ).distinct()

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())

    return render(request, 'products/product_list.html', {
        'products': products,
        'cart_count': cart_count,
        'categories': categories,
        'selected_category': category,
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {
        'product': product
    })


def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('product_list')

def cart(request):
    cart_data = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=product_id)

        item_total = product.price * quantity
        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    return render(request, 'products/cart.html', {
        'products': products,
        'total': total,
    })
def increase_quantity(request, id):
    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def decrease_quantity(request, id):
    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')

def checkout(request):
    cart_data = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=product_id)

        item_total = product.price * quantity
        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')

        Order.objects.create(
            name=name,
            phone=phone,
            email=email,
            address=address,
            city=city,
            pincode=pincode,
            total=total,
        )

        request.session['cart'] = {}
        request.session.modified = True

        return render(request, 'products/order_success.html', {
            'name': name,
            'total': total,
        })

    return render(request, 'products/checkout.html', {
        'products': products,
        'total': total,
    })
def payment(request):
    cart_data = request.session.get('cart', {})

    products = []
    total = 0

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=product_id)

        item_total = product.price * quantity
        total += item_total

        products.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
        })

    return render(request, 'products/payment.html', {
        'products': products,
        'total': total,
    })
