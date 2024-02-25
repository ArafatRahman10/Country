from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ['name_continent']

@admin.register(Pays)
class PaysAdmin(admin.ModelAdmin):
    list_display = ['name_pays','space','population','device','code',]