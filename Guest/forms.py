from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    name = forms.CharField(max_length=25)
    number = forms.CharField(max_length=17)
    location = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'name', 'number', 'location', 'city', 'state', 'password1', 'password2')
