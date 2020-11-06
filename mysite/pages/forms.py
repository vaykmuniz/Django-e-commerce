from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.forms import widgets

from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

        widgets = {
            'login': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}) 
        }

class RegisterForm(UserCreationForm):

    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label=("Password"), widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label=("Password confirmation"), widget = forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
