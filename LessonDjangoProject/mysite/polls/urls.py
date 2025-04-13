from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # например: /polls/
    path('', views.index, name='index'),
    # например: /polls/5/

    path('<int:question_id>/', views.detail, name='detail'),
    # например: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # например: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('registr/', views.registr, name='registr'),
    path('onas/', views.onas, name='onas'),
    path('sponsor/', views.sponsor, name='sponsor'),
    path('Seller/', views.Seller, name='Seller'),
]
