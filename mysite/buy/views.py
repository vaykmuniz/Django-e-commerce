from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserOrder
from products.models import Product

# Create your views here.

@login_required(login_url='login')
def cart_view(request):
    try:
        order = UserOrder.objects.all().filter(user = request.user)

        sum = 0
        for itens in order:
            sum = sum + itens.order.price
        context = {'cart': order, 'total': sum}
    except:
        context = {}
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def cart_delete(request, item_id):
    try:
        item = UserOrder.objects.get(id = item_id)
        if item.user == request.user:
            item.delete()
            messages.success(request, 'Item removed from cart!')
            return redirect('cart')
    except:
        return redirect('cart')

@login_required(login_url='login')
def add_item_cart(request, item):
    try:
        product = Product.objects.get(id = item)
        UserOrder.objects.create(user=request.user, order=product)
        messages.success(request, 'Item added to cart!')
        return redirect('cart')
    except:
        return redirect('cart')