from django.db import models
from django.contrib import admin

class TestUser(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Client(models.Model):
    user_login = models.CharField(max_length=70)
    user_passwold = models.CharField(max_length=20)
    user_wallet = models.CharField(max_length=50)

class nation(models.Model):
    nation_name = models.CharField(max_length=70)

class tanks(models.Model):
    tanks_title = models.CharField(max_length=70)
    tanks_nation = models.ForeignKey(nation, on_delete=models.CASCADE)
    tanks_cost = models.CharField(max_length=70)

class favorites(models.Model):
    favorites_user = models.ForeignKey(Client, on_delete=models.CASCADE)
    favorites_tanks = models.ForeignKey(tanks, on_delete=models.CASCADE)

class corzine(models.Model):
    corzine_user = models.ForeignKey(Client, on_delete=models.CASCADE)
    corzine_tanks = models.ForeignKey(tanks, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date pokupki')
