from django.http import JsonResponse
from django.shortcuts import render
from .basket import Basket
from django.shortcuts import get_object_or_404
from store.models import Product


# Create your views here.
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response

def basket_change(request):
    basket = Basket(request)
    if request.POST.get('action') == 'remove':
         product_id = int(request.POST.get('productid'))
         basket.remove(product=product_id)
    elif request.POST.get('action') == 'update':
         product_id = int(request.POST.get('productid'))
         product_qty = int(request.POST.get('productqty'))
         basket.update(product=product_id, qty=product_qty)
    basketqty = basket.__len__()
    baskettotal = basket.get_all_items_totall()
    response = JsonResponse({'qty': basketqty, 'subtotal':baskettotal})
    return response
    