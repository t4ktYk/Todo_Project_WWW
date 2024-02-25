from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User

from .models import Task

import datetime



class TaskCreationForm(forms.ModelForm):


    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add task', 'style': 'width: 300px; font-size: 14px; padding: 5px'}))

    class Meta:
        model = Task
        fields = ["description", ]





class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        username = UsernameField(widget=forms.TextInput(
            attrs={
                'class': 'form-login-username', 'id': 'name',
                'placeholder': 'Username',
            }))
        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-login-password', 'id': 'pass'}
        ))




class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        username = UsernameField(widget=forms.TextInput(
            attrs={
                'class': 'form-login-username', 'id': 'name',
            }))

        email = forms.EmailField(widget=forms.EmailInput(
            attrs={
                'class': 'form-login-email', 'id': 'email'
            }
        ))

        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-login-password', 'id': 'pass1'
            }
        ))

        password = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class': 'form-login-password', 'id': 'pass2'
            }
        ))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']