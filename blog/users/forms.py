from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#these fields will be unpacked in register.html page
class RegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
