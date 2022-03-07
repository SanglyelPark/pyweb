from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    email = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email']