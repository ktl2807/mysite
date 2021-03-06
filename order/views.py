from django.shortcuts import render
from django.http.response import JsonResponse

from basket.basket import Basket
from .models import Order, Order_item
# Create your views here.


def addOrder(request):
    basket = Basket(request)
    if request.POST.get('add')=='post':
        order_key = request.POST.get('order_key')
        user_id = request.user.id
        baskettotal = basket.get_total_price()
    if Order.objects.filter(order_key=order_key).exists():
            pass
    else:
        order = Order.objects.create(user_id=user_id, full_name='name', total_paid=baskettotal, order_key=order_key)
        order_id = order.pk

        for item in basket:
            Order_item.objects.create(order_id=order_id, product=item['product'], price=item['price'], quantity=item['qty'])

    response = JsonResponse({'success': 'Return something'})
    return response

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders