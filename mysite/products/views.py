from django.shortcuts import render
from .models import Product

# Create your views here.

def product_view(request):
    all_products = Product.objects.all()
    print(type(all_products))
    a = {
        'product': all_products}
    return render(request, 'home.html', a)

def busca_view(request):

    if request.method == 'GET':
        busca = request.GET.get('busca')
        resultados = Product.objects.filter(title = busca.capitalize())
    
        context = {'product': resultados }
        return render(request, 'busca.html', context) 

    return render(request, 'busca.html', {})  