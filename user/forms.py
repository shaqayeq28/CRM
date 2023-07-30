from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import Lead, Client


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'priority', 'status', 'description']


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'description']
