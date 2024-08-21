from django import forms
from django.contrib.auth.forms import UserCreationForm



class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "id": "username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password"
            }
        )
    )

