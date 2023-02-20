from django.shortcuts import render, redirect
import os
import stripe
from dotenv import load_dotenv, find_dotenv

from main.models import Item

load_dotenv(find_dotenv())
stripe.api_key = os.getenv('API_SECRET_KEY')
server = os.getenv('SERVER')


def create_checkout_session(request):
    product_name = request.GET.get('prod')
    product_price = request.GET.get('price')
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product_name,
                },
                'unit_amount': product_price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f"{server}success.html",
        cancel_url=f"{server}cancel.html",
    )
    return redirect(session.url, code=303)


def home_page(request):
    products = Item.objects.all()
    return render(request, 'home.html', {'products': products})


def success(request):
    return render(request, 'success')


def cancel(request):
    return render(request, 'cancel')
