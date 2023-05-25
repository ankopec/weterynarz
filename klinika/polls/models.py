from django.db import models
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers import PhoneNumber
import phonenumbers
from django.utils import timezone
from django.utils import formats

class Pacjenci(models.Model):
    class Meta:
        ordering=['imie_pacjenta','nazwisko_własciciela']
    imie_pacjenta = models.CharField(max_length=30)
    #id_pacjenta = models.IntegerField()
    class gatunek(models.TextChoices):
        PIES = ("pies"),
        KOT = ("kot"),
        KRÓLIK = ("królik"),
        ŚWINKA_MORSKA = ("świnka morska"),
        CHOMIK = ("chomik"),

    gatunek = models.CharField(max_length=20,
                               choices=gatunek.choices,
                               default=gatunek.PIES,)
    data_urodzenia = models.DateField(max_length=30)
    #wiek = models.IntegerField()
    class plec(models.TextChoices):
        SAMIEC = ("samiec"),
        SAMICA = ("samica"),
    plec = models.CharField(max_length=30,
                            choices=plec.choices,
                            default=plec.SAMICA)
    telefon = PhoneNumberField()
    #telefon = models.CharField(default='Brak danych', max_length=9)
    email = models.EmailField(max_length=50, blank=True, unique=True)
    imie_własciciela = models.CharField(default='Brak danych', max_length=60)
    nazwisko_własciciela = models.CharField(max_length=100)
    adres = models.TextField()
    def __str__(self):
        return f'{self.imie_pacjenta} {self.nazwisko_własciciela} ({self.telefon})'

class Weterynarz(models.Model):
    imie_weterynarza = models.CharField(max_length=50)
    nazwisko_weterynarza = models.CharField(max_length=100)
    telefon = PhoneNumberField(default='Brak danych')
    pwzNumer = models.CharField(default='Brak danych',max_length=5)
    def __str__(self):
        return f'{self.imie_weterynarza} {self.nazwisko_weterynarza} '

#class Pacjent(models.Model):
  #  class Meta:
   #     ordering=['imie_pacjenta','nazwisko_własciciela']
   # imie_pacjenta = models.CharField(max_length=30)
    #id_pacjenta = models.IntegerField()
    #class gatunek(models.TextChoices):
     #   PIES = ("pies"),
      #  KOT = ("kot"),
       # KRÓLIK = ("królik"),
       # ŚWINKA_MORSKA = ("świnka morska"),
        #CHOMIK = ("chomik"),

   # gatunek = models.CharField(max_length=20,
    #                           choices=gatunek.choices,
     #                          default=gatunek.PIES,)
    #data_urodzenia = models.DateField(max_length=30)
    #wiek = models.IntegerField()
    #class plec(models.TextChoices):
    #    SAMIEC = ("samiec"),
        SAMICA = ("samica"),
    #plec = models.CharField(max_length=30,
       #                     choices=plec.choices,
     #                       default=plec.SAMICA)
   # telefon = PhoneNumberField()
    #telefon = models.CharField(default='Brak danych', max_length=9)
    #email = models.EmailField(max_length=50, blank=True, unique=True)
    #imie_własciciela = models.CharField(default=None, max_length=60)
    #nazwisko_własciciela = models.CharField(max_length=100)
    #adres = models.TextField()
    #def __str__(self):
    #    return f'{self.imie_pacjenta} {self.nazwisko_własciciela} ({self.telefon})'






#class Rachunki(models.Model):
 #   id_lekarza = models.IntegerField()
  #  id_pacjenta = models.IntegerField()
    #pacjent= models.ForeignKey(Pacjent, on_delete=models.CASCADE,default=None)
    #weterynarz = models.ForeignKey(Weterynarz, on_delete=models.CASCADE, default=None)
    #data_wystawienia = models.DateField(max_length=30)
    #cena_uslugi = models.DecimalField(max_digits=10, decimal_places=2)
    #def get_formatted_price(self):
    #    return f'{formats.number_format(self.cena_uslugi)}{zł}'
   # diagnoza=models.CharField(max_length=500)
   # podane_leki=models.CharField(max_length=100,default='Brak danych')
  #  zalecenia=models.CharField(max_length=300, default='Brak danych')


class Rachunek(models.Model):
    pacjenci = models.ForeignKey(Pacjenci, on_delete=models.CASCADE, default=None)
    weterynarz = models.ForeignKey(Weterynarz, on_delete=models.CASCADE, default=None)
    data_wystawienia = models.DateField(max_length=30)
    cena_uslugi = models.DecimalField(max_digits=10, decimal_places=2)

    def get_formatted_price(self):
        return f'{formats.number_format(self.cena_uslugi)}{zł}'

    diagnoza = models.CharField(max_length=500)
    podane_leki = models.CharField(max_length=100, default='Brak danych')
    zalecenia = models.CharField(max_length=300, default='Brak danych')
    plik_dicom=models.FileField(upload_to='static/dicom',blank=True,null=True)