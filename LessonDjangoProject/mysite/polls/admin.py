
from django.contrib import admin

# Register your models here.

from .models import Client, nation, tanks, favorites, corzine, TestUser

admin.site.register(Client)
admin.site.register(nation)
admin.site.register(tanks)
admin.site.register(favorites)
admin.site.register(corzine)
admin.site.register(TestUser)