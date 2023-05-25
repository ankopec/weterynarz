from django.contrib import admin
from django.urls import include, path
from . import views
from .views import home,cennik
from .views import Pacjent
from .views import Lekarz_home

urlpatterns = [
    #path('index/', views.index),
    #path('', views.home, name = "home"),
    path('', home.home, name="home"),
    path('', home.home, name="home"),

    path('lekarz/dodaj/', Pacjent.dodaj, name="pacjent_dodaj"),
    path('lekarz/pobierz_liste/', Pacjent.pobierz_liste, name="pacjent_pobierz_liste"),
    path('lekarz/', Lekarz_home.lekarz_home, name="Lekarz"),
    path('lekarz/edytuj/<int:pacjent_id>/', Pacjent.edytuj, name="pacjent_edytuj"),
    path('lekarz/lista_edytuj/', Pacjent.lista_edytuj, name='pacjent_lista_edytuj'),
    path('lekarz/lista_usun/', Pacjent.lista_usun, name='pacjent_lista_usun'),
    path('lekarz/lista_solo/', Pacjent.lista_solo, name='pacjent_lista_solo'),
    path('lekarz/usun/<int:pacjent_id>/', Pacjent.usun, name="pacjent_usun"),
    path('lekarz/rachunek_dodaj/', Pacjent.dodaj_rachunek, name="dodaj_rachunek"),

    path('pacjent/', Pacjent.pacjent_home, name="Pacjent"),
    path('pacjent/rachunek/', Pacjent.lista_rachunkow, name="rachunek"),
    path('pacjent/rachunek/pobierz_rachunek/<int:rachunek_id>/', Pacjent.pobierz_rachunek, name="pacjent-pobierz_rachunek"),

    path('cennik/',cennik.cennik, name="cennik"),
    path('regulamin/', cennik.regulamin, name="regulamin"),
    path('media/', cennik.media, name="media"),


]