
from django.contrib import admin

# Register your models here.

from .models import Client, nation, tanks, favorites, corzine

admin.site.register(nation)
admin.site.register(tanks)
admin.site.register(favorites)
admin.site.register(corzine)
admin.site.register(Client)