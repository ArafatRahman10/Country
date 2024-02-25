from django.shortcuts import render, redirect
from .models import *

from .form import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def addcontinent(request):
    if request.method == "POST":
        form = ContinentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContinentForm()
        return render(request, 'addcontinent.html', {'form':form})
