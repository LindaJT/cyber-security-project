from django.forms import ModelForm
from django import forms
from .models import Person

class RegisterForm(ModelForm):

    class Meta:
        model = Person
        fields = ['username', 'password']

class LoginForm(ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password']