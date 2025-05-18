from dbm import error

from .models import Client
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm, LoginForm


def index(request):
    return render(request, 'polls/index.html')


def onas(request):
    return render(request, 'polls/onas.html')


def sponsor(request):
    return render(request, 'polls/sponsor.html')


def seller(request):
    return render(request, 'polls/Seller.html')


def ss(request):
    return render(request, 'polls/ss.html')

@csrf_exempt
def login(request):
    return  render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = Client(login=username, password=password)
        user.save()
        return render(request, 'login.html')
    else:
        return render(request, 'register.html')

@csrf_exempt
def vhod(request):
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        try:
            user = Client.objects.get(Login=username, password=password)
            return render(request, "index.html", {'username': username})
        except Client.DoesNotExist:
            return render(request, 'register.html', {'error': 'peredelavai'})
    return render(request, 'register.html')