from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User

import datetime



class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        username = UsernameField(widget=forms.TextInput(
            attrs={
                'class': 'form-login-username', 'id': 'name',
            }))
        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-login-password', 'id': 'pass'}
        ))




class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']