import datetime
from datetime import timedelta
import random

from django.core.management.base import BaseCommand

from polls.models import Rachunek,Pacjenci,Weterynarz

def losowa_data_wystawienia():
    start = datetime.date(2012, 1, 1)
    end = datetime.date(2022, 1, 5)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

diagnoza=['zapalenie ucha zewnętrznego','kamienie moczowe','skręt żołądka','alergia skórna','choroba nerek','obce ciało w układzie pokarmowym',
           'zranienie opuszki','rana szarpana','kleszcz','usunięcie zęba']
podane_leki=['amoksycylina','cefaleksyna','pyrantel','fenbendazol','kortyzon','predizon','famcyklowir',
              'pimobendan','furosemid','tetracyklina','ivermektyna']
zalecenia=['zmiana opatrunków','spokojne spacery','ograniczenie ruchu','kontrola za 2 dni i za tydzień','regularna aktywność fizyczna','regularne szczepienia',
           'zbilansowana dieta']


class Command(BaseCommand):
    help = "Dodaje losowo wybrane rachunki"

    def add_arguments(self, parser):
        parser.add_argument("N",type=int)

    def handle(self, *args, **options):
        for i in range(options['N']):

            pacjenci = Pacjenci.objects.all()
            pacjentt = random.choice(pacjenci)
            weterynarze=Weterynarz.objects.all()
            weterynarzz=random.choice(weterynarze)
            cenaa = str(random.randint(50, 500))
            diagnozaa=random.choice(diagnoza)
            podane_lekii=random.choice(podane_leki)
            zaleceniaa=random.choice(zalecenia)

            rachunki = Rachunek(pacjenci=pacjentt,
                                weterynarz=weterynarzz,
                                data_wystawienia=losowa_data_wystawienia(),
                                cena_uslugi=int(cenaa),
                                diagnoza=diagnozaa,
                                podane_leki=podane_lekii,
                                zalecenia=zaleceniaa)

            rachunki.save()
            print(rachunki)
