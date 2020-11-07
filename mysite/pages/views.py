from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            usr = request.POST.get('username')
            pswd = request.POST.get('password')

            user = authenticate(request, username = usr, password = pswd)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Hello, ' + usr + '!')
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorret')

        context = {}
        return render(request, "login.html", context)

@login_required(login_url='login')
def logout_pag(request):
    logout(request)
    messages.success(request, 'Logout!')
    return redirect('home')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()

        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('home')

        context = {'form':form}
        return render(request, "register.html", context)
