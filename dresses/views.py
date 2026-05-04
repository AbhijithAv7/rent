from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .models import *


def home(request):
    return render(request, 'home.html')


@login_required
def product_list(request):
    dresses = Dress.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')

    if query:
        dresses = dresses.filter(name__icontains=query)

    return render(request, 'products.html', {
        'dresses': dresses,
        'categories': categories
    })

@login_required
def product_detail(request, id):
    dress = get_object_or_404(Dress, id=id)

    if request.method == "POST":
        days = int(request.POST.get("days"))
        total_price = request.POST.get("total_price")

        Order.objects.create(
            user=request.user,
            dress=dress,
            days=days,
            total_price=total_price
        )

        return redirect("products")

    return render(request, "product_detail.html", {"dress": dress})

@login_required
def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    dresses = Dress.objects.filter(category=category)

    return render(request, 'products.html', {
        'dresses': dresses,
        'selected_category': category
    })

def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    from .models import Dress
    dress = Dress.objects.get(id=id)

    if str(id) in cart:
        cart[str(id)]['days'] += 1   
    else:
        cart[str(id)] = {
            'name': dress.name,
            'price': float(dress.price_per_day),
            'image': dress.image.url,
            'days': 1   
        }

    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        total += item['price'] * item['days']

    return render(request, 'cart.html', {
        'cart': cart,
        'total': total
    })

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    return redirect('cart') 

def update_cart(request, id):
    if request.method == "POST":
        days = int(request.POST.get('days'))

        cart = request.session.get('cart', {})

        if str(id) in cart:
            cart[str(id)]['days'] = days

        request.session['cart'] = cart

    return redirect('cart')