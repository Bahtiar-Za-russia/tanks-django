from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser


class Client(AbstractUser):
    USERNAME_FIELD = 'login'  # или 'email', если добавите это поле
    REQUIRED_FIELDS = []  # обязательные поля при создании пользователя

    class Meta:
        db_table = 'clients'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = Client
        fields = ( 'email', 'password')


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)