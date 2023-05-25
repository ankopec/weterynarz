# Generated by Django 4.2.1 on 2023-05-20 17:49

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_rename_pacjent_rachunki_pacjent1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacjent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie_pacjenta', models.CharField(max_length=30)),
                ('gatunek', models.CharField(choices=[('pies', 'Pies'), ('kot', 'Kot'), ('królik', 'Królik'), ('świnka morska', 'Świnka Morska'), ('chomik', 'Chomik')], default='pies', max_length=20)),
                ('data_urodzenia', models.DateField(max_length=30)),
                ('plec', models.CharField(choices=[('samiec', 'Samiec'), ('samica', 'Samica')], default='samica', max_length=30)),
                ('telefon', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=50, unique=True)),
                ('imie_własciciela', models.CharField(default='Brak danych', max_length=60)),
                ('nazwisko_własciciela', models.CharField(max_length=100)),
                ('adres', models.TextField()),
            ],
            options={
                'ordering': ['imie_pacjenta', 'nazwisko_własciciela'],
            },
        ),
        migrations.RemoveField(
            model_name='rachunki',
            name='pacjent1',
        ),
        migrations.AddField(
            model_name='rachunki',
            name='pacjent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.pacjent'),
        ),
    ]