from django.urls import path
from django.contrib.auth import views as views_auth

from . import views, forms


urlpatterns = [
    path('', views.index, name='index'),


    path('login/', views_auth.LoginView.as_view(
        authentication_form=forms.UserLoginForm),
        name='login'
    ),
    path('register/', views.register, name='register'),
    path('logout/', views.cs_logout, name='logout'),
]