from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('onas/', views.onas, name='onas'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('seller/', views.seller, name='seller'),
    path('ss/', views.ss, name='ss'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('USA.html', views.usa, name='usa'),
    path('WB.html', views.wb, name='wb'),
    path('GER.html', views.ger, name='ger'),
    path('FRC.html', views.frc, name='frc'),
    path('CH.html', views.ch, name='ch'),
    path('pokupka.html', views.pokupka, name='pokupka'),
]