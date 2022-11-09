from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = Customer
        fields = ['name','email','passw','passw','imagen']

    imagen = forms.ImageField(label="Avatar", required=False, widget=forms.FileInput(attrs={'class':'form-control'}))

    