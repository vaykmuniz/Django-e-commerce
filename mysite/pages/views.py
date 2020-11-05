from django.shortcuts import render
from .forms import CustomerForm

# Create your views here.

def login_view(request, *args, **kwargs):
    
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "login.html", context)