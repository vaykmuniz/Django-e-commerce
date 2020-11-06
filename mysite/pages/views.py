from django.shortcuts import render
from .forms import CustomerForm, RegisterForm
#from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_view(request, *args, **kwargs):
    
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "login.html", context)

def register_view(request):
    
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "register.html", context)