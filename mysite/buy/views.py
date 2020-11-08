from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from pprint import pprint

from .models import UserOrder

# Create your views here.

@login_required(login_url='login')
def cart_view(request):

    order = UserOrder.objects.all().filter(user = request.user)
    context = {'cart': order}
    return render(request, 'cart.html', context)