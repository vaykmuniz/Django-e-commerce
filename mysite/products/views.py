from django.shortcuts import render
from .models import Product

# Create your views here.

def product_view(request):
    all_products = Product.objects.all()
    print(type(all_products))
    a = {
        'product': all_products}
    return render(request, 'home.html', a)