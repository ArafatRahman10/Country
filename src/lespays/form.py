from django.forms import ModelForm
from .models import *
from django import forms

class ContinentForm(ModelForm):
    class Meta:
        model = Continent
        fields = ('name_continent',)
   

class PaysForm(ModelForm):
    class Meta:
        model = Pays
        fields = '__all__'
