import csv
from datetime import datetime
from django.middleware.csrf import get_token
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect, render
from polls.forms import FormularzPacjenta, FiltrPacjentow, FormularzRachunkow, FiltrRachunkow
from polls.models import Pacjenci, Rachunek, Weterynarz

def dodaj(request):
    if request.method == 'POST':
        formularz = FormularzPacjenta(request.POST)
        if formularz.is_valid():
            print("Formularz jest poprawny")
            print("Zapisujemy pocjenta")
            print(formularz.cleaned_data)
            formularz.save()
            messages.success(request, "Pacjenta dodany.")
            return redirect('pacjent-lista')
        else:
            print("Formularz ma błędy")
    else:
        formularz = FormularzPacjenta()

    return render(request, 'lekarz/dodaj_pacjenta.html',
                  {
                      'formularz':formularz
                  })

def usun(request, pacjent_id):
    pacjent = Pacjenci.objects.get(pk=pacjent_id)
    pacjent.delete()
    messages.success(request, 'Pacjent został usunięty z bazy')

    return redirect('pacjent_lista')

def edytuj(request, pacjent_id):
    pacjent = Pacjenci.objects.get(pk=pacjent_id)

    if request.method == 'POST':
        formularz = FormularzPacjenta(request.POST, instance=pacjent)
        if formularz.is_valid():
            print("Formularz jest poprawny")
            print("Zapisujemy pacjenta do bazy")
            print(formularz.cleaned_data)
            formularz.save()
            # przekierowanie do listy pacjentów
            messages.success(request, "Pacjent zapisany.")
            return redirect('pacjent_lista')
        else:
            print("Formularz ma błędy")
    else:
        formularz = FormularzPacjenta(instance=pacjent)

    return render(request, 'lekarz/edytuj_pacjenta.html', {
        'formularz': formularz
    })


def pacjent_home(request):
    #browser = request.headers['User-Agent']

    return render(request, 'pacjent/PacjentHome.html')

def lista_edytuj(request):
    pacjenci=Pacjenci.objects.all().order_by('imie_pacjenta','nazwisko_własciciela')

    formularz_wyszukiwania=FiltrPacjentow(request.GET)
    if formularz_wyszukiwania.is_valid():
        cd = formularz_wyszukiwania.cleaned_data
        if cd['imie_pacjenta']:
            pacjenci=pacjenci.filter(imie_pacjenta__contains=cd['imie_pacjenta'])
        if cd['imie_wlasciciela']:
            pacjenci = pacjenci.filter(imie_wlasciciela__icontains=cd['imie_własciciela'])
        if cd['nazwisko_wlasciciela']:
            pacjenci = pacjenci.filter(nazwisko_własciciela__contains=cd['nazwisko_wlasciciela'])
        if cd['gatunek']:
            pacjenci = pacjenci.filter(gatunek__iexact=cd['gatunek'])
        if cd['plec']:
            pacjenci = pacjenci.filter(plec__contains=cd['plec'])

    paginator = Paginator(pacjenci, 15)
    nr_strony = request.GET.get('strona', 1)

    if request.method == 'POST' and 'wyczysc' in request.POST:
        formularz_wyszukiwania.initial['plec'] = None
        formularz_wyszukiwania.initial['gatunek'] = None

    return render(request, 'pacjent/lista_pacjentow.html', {
        'strona_pacjentow': paginator.get_page(nr_strony),
        'formularz_wyszukiwania': formularz_wyszukiwania
    })

def lista_solo(request):
    pacjenci=Pacjenci.objects.all().order_by('imie_pacjenta','nazwisko_własciciela')

    formularz_wyszukiwania=FiltrPacjentow(request.GET)
    if formularz_wyszukiwania.is_valid():
        cd = formularz_wyszukiwania.cleaned_data
        if cd['imie_pacjenta']:
            pacjenci=pacjenci.filter(imie_pacjenta__contains=cd['imie_pacjenta'])
        if cd['imie_wlasciciela']:
            pacjenci = pacjenci.filter(imie_wlasciciela__icontains=cd['imie_własciciela'])
        if cd['nazwisko_wlasciciela']:
            pacjenci = pacjenci.filter(nazwisko_własciciela__contains=cd['nazwisko_wlasciciela'])
        if cd['gatunek']:
            pacjenci = pacjenci.filter(gatunek__iexact=cd['gatunek'])
        if cd['plec']:
            pacjenci = pacjenci.filter(plec__contains=cd['plec'])

    paginator = Paginator(pacjenci, 15)
    nr_strony = request.GET.get('strona', 1)

    if request.method == 'POST' and 'wyczysc' in request.POST:
        formularz_wyszukiwania.initial['plec'] = None
        formularz_wyszukiwania.initial['gatunek'] = None

    return render(request, 'pacjent/listaP_solo.html', {
        'strona_pacjentow': paginator.get_page(nr_strony),
        'formularz_wyszukiwania': formularz_wyszukiwania
    })

def lista_usun(request):
    pacjenci=Pacjenci.objects.all().order_by('imie_pacjenta','nazwisko_własciciela')

    formularz_wyszukiwania=FiltrPacjentow(request.GET)
    if formularz_wyszukiwania.is_valid():
        cd = formularz_wyszukiwania.cleaned_data
        if cd['imie_pacjenta']:
            pacjenci=pacjenci.filter(imie_pacjenta__contains=cd['imie_pacjenta'])
        if cd['imie_wlasciciela']:
            pacjenci = pacjenci.filter(imie_wlasciciela__icontains=cd['imie_własciciela'])
        if cd['nazwisko_wlasciciela']:
            pacjenci = pacjenci.filter(nazwisko_wlasciciela_conatins=cd['nazwisko_wlasciciela'])
        if cd['gatunek']:
            pacjenci = pacjenci.filter(gatunek__iexact=cd['gatunek'])
        if cd['plec']:
            pacjenci = pacjenci.filter(plec__contains=cd['plec'])

    paginator = Paginator(pacjenci, 15)
    nr_strony = request.GET.get('strona', 1)

    return render(request, 'pacjent/lista_pacjentow_usun.html', {
        'strona_pacjentow': paginator.get_page(nr_strony),
        'formularz_wyszukiwania': formularz_wyszukiwania
    })

def pobierz_liste(request):
    odpowiedz = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="lista_pacjentow.txt"'},
    )

    writer = csv.writer(odpowiedz, delimiter=';')
    writer.writerow(['Imie Pacjenta', 'Nazwisko właściciela', 'Imie właściciela'])
    for pacjent in Pacjenci.objects.all():
        writer.writerow([pacjent.imie_pacjenta, pacjent.imie_własciciela, pacjent.nazwisko_własciciela])

    return odpowiedz

def lista_rachunkow(request):
    rachunek = Rachunek.objects.all().order_by('pacjenci','weterynarz')

    formularz_wyszukiwania=FiltrRachunkow(request.GET)
    if formularz_wyszukiwania.is_valid():
        cd = formularz_wyszukiwania.cleaned_data
        if cd['imie_pacjenta']:
            rachunek=rachunek.filter(pacjenci__imie_pacjenta__icontains=cd['imie_pacjenta'])
        if cd['weterynarz']:
            rachunek = rachunek.filter(weterynarz=cd['weterynarz'])


    paginator = Paginator(rachunek, 15)
    nr_strony = request.GET.get('strona', 1)

    return render(request, 'pacjent/lista_rachunkow.html', {
        'strona_rachunkow': paginator.get_page(nr_strony),
        'formularz_wyszukiwania': formularz_wyszukiwania,
        'rachunki': rachunek
    })

def pobierz_rachunek(request, rachunek_id):
    rachunek=Rachunek.objects.get(pk=rachunek_id)
    if rachunek.plik_dicom:
        file_path = rachunek.plik_dicom.path
        with open(file_path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/dicom')
            response['Content-Disposition'] = f'attachment; filename="{rachunek.plik_dicom.name}"'
            return response
    else:
        return HttpResponse("Brak pliku DICOM.")

def dodaj_rachunek(request):
    if request.method == 'POST':
        rachunek = FormularzRachunkow(request.POST)
        if rachunek.is_valid():
            print("Formularz jest poprawny")
            print("Zapisujemy rachunek")
            print(rachunek.cleaned_data)
            rachunek.save()
            messages.success(request, "Rachunek dodany.")
            return redirect('rachunek')
        else:
            print("Formularz ma błędy")
    else:
            rachunek = FormularzRachunkow()

            return render(request, 'lekarz/dodaj_rachunek.html',{'formularz':rachunek})