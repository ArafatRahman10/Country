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

def continents_list(request):
    continents = Continent.objects.all()
    return render(request, 'continents_list.html', {'continents': continents})


def delete_continent(request, continent_id):
    continent = Continent.objects.get(id=continent_id)
    continent.delete()
    return redirect('continents_list')

def edit_continent(request, continent_id):
    continent = Continent.objects.get(id=continent_id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        continent.name_continent = new_name
        continent.save()
        return redirect('continents_list')

    return render(request, 'edit_continent.html', {'continent': continent})

def addpays(request):
    if request.method == "POST":
        form = PaysForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaysForm()
        return render(request, 'addpays.html', {'form':form})    

def edit_pays(request, pays_id):
    pays = Pays.objects.get(id=pays_id)

    if request.method == 'POST':
        new_name = request.POST.get('new_name')
        pays.name_pays = new_name
        pays.space = new_name
        pays.population = new_name
        pays.device = new_name
        pays.code = new_name
        pays.Continent = new_name
        pays.save()
        return redirect('pays_list')

    return render(request, 'edit_pays.html', {'pays': pays})

def pays_list(request):
    payss = Pays.objects.all()
    return render(request, 'pays_list.html', {'payss': payss})

def delete_pays(request, pays_id):
    pays = Pays.objects.get(id=pays_id)
    pays.delete()
    return redirect('pays_list')



    