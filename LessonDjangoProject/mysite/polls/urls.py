from django.urls import path
from . import views

# app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('onas/', views.onas, name='onas'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('seller/', views.seller, name='seller'),
    path('ss/', views.ss, name='ss'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]