from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Client

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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Используем email как username
            user.save()
            auth_login(request, user)
            return redirect('polls:index')
        else:
            # Вывод ошибок формы
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Используем username как email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('polls:index')
        # Вывод ошибок формы
        for error in form.get_invalid_login_error():
            messages.error(request, error)
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})

def usa(request):
    return render(request, 'polls/USA.html')

def wb(request):
    return render(request, 'polls/WB.html')

def ger(request):
    return render(request, 'polls/GER.html')

def frc(request):
    return render(request, 'polls/FRC.html')

def ch(request):
    return render(request, 'polls/CH.html')