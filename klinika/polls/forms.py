from django.core.validators import RegexValidator
from django.forms import Form, CharField, IntegerField, DateField, ModelForm, HiddenInput, ModelChoiceField,forms
from django import forms
from polls.models import Pacjenci, Rachunek, Weterynarz

class FormularzPacjenta(ModelForm):
    class Meta:
        model = Pacjenci
        fields = '__all__'


class FiltrPacjentow(Form):
    imie_pacjenta = CharField(label='Imię pacjenta', required=False)
    imie_wlasciciela = CharField(label='Imię wlasciciela', required=False)
    nazwisko_wlasciciela = CharField(label='nazwisko wlasciciela', required=False)
    #gatunek = CharField(label='gatunek', required=False)


    class Gatunki(forms.Form):
        GATUNKI =[
            ("", "---------"),
            ("pies", "Pies"),
            ("kot", "Kot"),
            ("królik", "Królik"),
            ("świnka_morska", "Świnka morska"),
            ("chomik", "Chomik"),
        ]
    gatunek = forms.ChoiceField(choices=Gatunki.GATUNKI, required=False, widget=forms.Select)
    class Plec(forms.Form):
        PLEC=[
            ("", "---------"),
            ("samica","Samica"),
            ("samiec","Samiec"),
        ]
    plec = forms.ChoiceField(choices=Plec.PLEC, required=False, widget=forms.Select)
    email = CharField(label='email', required=False)

    def clean(self):
        cleaned_data = super().clean()
        plec = cleaned_data.get('plec')
        gatunek = cleaned_data.get('gatunek')

        if plec == '':
            cleaned_data['plec'] = None

        if gatunek == '':
            cleaned_data['gatunek'] = None

        return cleaned_data

class FormularzRachunkow(ModelForm):
    class Meta:
        model = Rachunek
        fields = '__all__'

class FiltrRachunkow(Form):
    imie_pacjenta=CharField(label='Imię_pacjenta', required=False)
    #weterynarz=forms.ChoiceField(choices=Weterynarz.nazwisko_weterynarza, required=False, widget=forms.Select)
    weterynarz = forms.ModelChoiceField(
        label='Weterynarz',
        queryset=Weterynarz.objects.all(),
        empty_label='---------',
        required=False
    )




    #weterynarz=CharField(label='Weterynarz', required=False)