
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# class Client(AbstractUser):
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

    # class Meta:
    #     db_table = 'clients'

class Client(models.Model):
    login = models.CharField(max_length=200, default="")
    password = models.CharField(max_length=200, default="")

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
