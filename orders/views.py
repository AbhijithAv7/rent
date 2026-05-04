import razorpay
from django.conf import settings
from django.shortcuts import render

def payment_page(request):
    cart = request.session.get('cart', {})
    total = 0

    for item in cart.values():
        total += item['price'] * item['days']

    amount = int(total * 100)  # convert to paise

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    return render(request, "payment.html", {
        "payment": payment,
        "total": total,
        "key": settings.RAZORPAY_KEY_ID
    })