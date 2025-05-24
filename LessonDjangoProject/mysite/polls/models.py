from django.contrib.auth.models import AbstractUser
from django.db import models

class Client(AbstractUser):
    # Делаем username необязательным и nullable
    username = models.CharField(max_length=150, null=True, blank=True, unique=False)
    
    # Устанавливаем email как основное поле для аутентификации
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # username не требуется, так как используем email

    class Meta:
        db_table = 'clients'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.email

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

