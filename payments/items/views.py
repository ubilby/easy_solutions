from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import stripe

from items.models import Item
from payments.settings import STRIPE_SECRET_KEY


def buy(request, item_id):
    stripe.api_key = STRIPE_SECRET_KEY
    item = get_object_or_404(Item, id=item_id)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=item.price,
        product_data={"name": item.name},
    )

    checkout_session = stripe.checkout.Session.create(
        line_items=[{
            'price': price.id,
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('items:item_succes')),
    )
    return redirect(checkout_session.url, code=303)


def item_detail(request, item_id):
    ...


def item_succes(request):
    template = 'completed.html'
    return render(request, template)
