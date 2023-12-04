from os import getenv

from django.shortcuts import get_object_or_404
import stripe

from items.models import Item


def buy(request, item_id):
    stripe.api_key = getenv('STRIPE_SECRET_KEY')
    item = get_object_or_404(Item, id=item_id)
    checkout_session = stripe.checkout.Session.create(
        line_items=[{
            'price': item.price,
            'quantity': 1,
        }]
    )
    return checkout_session.id


def item_detail(request, item_id):
    ...
