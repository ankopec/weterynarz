import datetime
from datetime import timedelta
import random

from django.core.management.base import BaseCommand

from polls.models import Pacjenci

imie_samica = ['Beza','Brandy','Bułka','Chili','Cookie','Delma','Fanta','Feta','Figa','Frytka',
               'Inka','Kama','Kawa','Kiwi','Kluska','Kola','Latte','Mamba','Milka','Mokka','Pajda',
               'Pepsi','Pita','Sushi','Tea','Toffi','Trufla','Alaska','Aruba','Brema','Capri',
               'Jawa','Costa','Elba','Etna','Nitra','Roma','Ryga','Tajga','Tonga','Wenus',
               'Bibi','Bunia','Buffy','Doda','Duffy','Fiona','Gaga','Gerda','Gloria','Lilo',
               'Luna', 'Peppa','Atena','Daphne','Diana','Gaja','Hebe','Juno','Kirke','Liv','Sawa',
               'Bożenka','Bronka','Frania','Ryśka','Zocha','Farsa','Mafia''Wiza','Zaza']
imie_samiec = ['Afro','Albin','Amor','Azor','Biszkopt','Bobik','Borys','Brutus','Cezar','Charlie',
               'Chester','Corso','Daktyl','Diego','Dolar','Drops','Edek','Eddy','Egon','Elvis',
               'Fafi','Fafik','Figiel','Flapi','Gaston','Gospel','Grafit','Gucio','Hamlet',
               'Lucky','Łapek','Łatek','Okruszek','Ozzie','Szarik','Szafran','Wafel','Yoda',
               'Kieł','Goofy','Kibic','Reksio','Rex','Scooby Doo','Snoopy','Śliniak','Tramp']

imiona_damskie = ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Krystyna', 'Barbara', 'Ewa', 'Elżbieta',
                  'Zofia', 'Janina', 'Teresa', 'Joanna', 'Magdalena', 'Monika', 'Jadwiga', 'Danuta', 'Irena', 'Halina',
                  'Helena', 'Beata', 'Aleksandra', 'Marta', 'Dorota', 'Marianna', 'Grażyna', 'Jolanta', 'Stanisława',
                  'Iwona', 'Karolina', 'Bożena', 'Urszula', 'Justyna', 'Renata', 'Alicja', 'Paulina', 'Sylwia',
                  'Natalia', 'Wanda', 'Agata', 'Aneta', 'Izabela', 'Ewelina', 'Marzena', 'Wiesława', 'Genowefa',
                  'Patrycja', 'Kazimiera', 'Edyta', 'Stefania']
imiona_meskie = ['Jan', 'Andrzej', 'Piotr', 'Krzysztof', 'Stanisław', 'Tomasz', 'Paweł', 'Józef', 'Marcin', 'Marek',
                 'Michał', 'Grzegorz', 'Jerzy', 'Tadeusz', 'Adam', 'Łukasz', 'Zbigniew', 'Ryszard', 'Dariusz', 'Henryk',
                 'Mariusz', 'Kazimierz', 'Wojciech', 'Robert', 'Mateusz', 'Marian', 'Rafał', 'Jacek', 'Janusz',
                 'Mirosław', 'Maciej', 'Sławomir', 'Jarosław', 'Kamil', 'Wiesław', 'Roman', 'Władysław', 'Jakub',
                 'Artur', 'Zdzisław', 'Edward', 'Mieczysław', 'Damian', 'Dawid', 'Przemysław', 'Sebastian', 'Czesław',
                 'Leszek', 'Daniel', 'Waldemar']
nazwiska = ['Nowak', 'Kowalski', 'Wiśniewski', 'Dąbrowski', 'Lewandowski', 'Wójcik', 'Kamiński', 'Kowalczyk',
            'Zieliński', 'Szymański', 'Woźniak', 'Kozłowski', 'Jankowski', 'Wojciechowski', 'Kwiatkowski', 'Kaczmarek',
            'Mazur', 'Krawczyk', 'Piotrowski', 'Grabowski', 'Nowakowski', 'Pawłowski', 'Michalski', 'Nowicki',
            'Adamczyk', 'Dudek', 'Zając', 'Wieczorek', 'Jabłoński', 'Król', 'Majewski', 'Olszewski', 'Jaworski',
            'Wróbel', 'Malinowski', 'Pawlak', 'Witkowski', 'Walczak', 'Stępień', 'Górski', 'Rutkowski', 'Michalak',
            'Sikora', 'Ostrowski', 'Baran', 'Duda', 'Szewczyk', 'Tomaszewski', 'Pietrzak', 'Marciniak', 'Wróblewski',
            'Zalewski', 'Jakubowski', 'Jasiński', 'Zawadzki', 'Sadowski', 'Bąk', 'Chmielewski', 'Włodarczyk',
            'Borkowski', 'Czarnecki', 'Sawicki', 'Sokołowski', 'Urbański', 'Kubiak', 'Maciejewski', 'Szczepański',
            'Kucharski', 'Wilk', 'Kalinowski', 'Lis', 'Mazurek', 'Wysocki', 'Adamski', 'Kaźmierczak', 'Wasilewski',
            'Sobczak', 'Czerwiński', 'Andrzejewski', 'Cieślak', 'Głowacki', 'Zakrzewski', 'Kołodziej', 'Sikorski',
            'Krajewski', 'Gajewski', 'Szymczak', 'Szulc', 'Baranowski', 'Laskowski', 'Brzeziński', 'Makowski',
            'Ziółkowski', 'Przybylski']

gatunek = ['pies','kot','chomik','świnka morska', 'królik']
plec = ['samiec','samica']

ulica = ['Piękna','Śliczna','Urocza','Krakoska','Ciasteczków','Specerowa','Psich ciasteczków','Parkowa','Kijowska']
miasto = ['Kraków','Myślenice','Wieliczka','Niepołomice','Dopczyce']
email = ['gmail.com','uAfgana.com','o2.pl','interia.pl','wp.pl']


def losowa_data_urodzenia():
    start = datetime.date(2010, 1, 1)
    end = datetime.date(2022, 1, 1)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

class Command(BaseCommand):
    help = "Dodaje losowo wybranych pacjentów"

    def add_arguments(self, parser):
        parser.add_argument("N",type=int)

    def handle(self, *args, **options):
        for i in range(options['N']):

            nazwisko=random.choice(nazwiska)
            if random.random()<0.5:
                imie_wlascicielaa = random.choice(imiona_damskie)
                if nazwisko.endswith('ski') or nazwisko.endswith('cki') or nazwisko.endswith('dzki'):
                     nazwisko = nazwisko.replace('ski', 'ska').replace('cki', 'cka').replace('dzki', 'dzka')
            else:
                imie_wlascicielaa = random.choice(imiona_meskie)

            plecc = random.choice(plec)
            if plecc.endswith('c'):
                imie_zwierz=random.choice(imie_samiec)
            else:
                imie_zwierz=random.choice(imie_samica)


            nr_tel = str(random.randint(500000001, 999999999))
            nr_domu = str(random.randint(1, 85))
            kod = str(random.randint(29, 33))
            #poc1 = str(random.randint(195, 630))
            #poc2 = str(random.randint(631, 899))
            poczt = str(random.randint(410, 890))
            gatunekk = random.choice(gatunek)


            miastoo=random.choice(miasto)
            ulicaa=random.choice(ulica)
            emaill=random.choice(email)


            pacjent = Pacjenci(imie_pacjenta = imie_zwierz,
                              gatunek=gatunekk,
                              data_urodzenia=losowa_data_urodzenia(),
                              plec=plecc,
                              telefon=nr_tel,
                              email=f'{imie_wlascicielaa}.{nazwisko}@{emaill}',
                              nazwisko_własciciela=nazwisko,
                              imie_własciciela=imie_wlascicielaa,
                              adres=f'{ulicaa} {nr_domu}   '
                                    f'{kod}-{poczt}   {miastoo}')
            pacjent.save()
            print(pacjent)

