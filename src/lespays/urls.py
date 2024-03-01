from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('addcontinent/', addcontinent, name='addcontinent'),
    path('continents_list/', continents_list , name='continents_list'),
    path('edit/<int:continent_id>/', edit_continent, name='edit_continent'),
    path('delete/<int:continent_id>/', delete_continent, name='delete_continent'),
    path('addpays/', addpays, name='addpays'),
    path('pays_list/', pays_list , name='pays_list'),
    path('edit/<int:pays_id>/', edit_pays, name='edit_pays'),
    path('delete/<int:pays_id>/', delete_pays, name='delete_pays'),

]

