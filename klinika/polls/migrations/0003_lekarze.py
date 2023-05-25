# Generated by Django 4.2.1 on 2023-05-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_remove_lekarz_imie_lekarza_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lekarze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie_lekarza', models.CharField(default='Brak danych', max_length=50)),
                ('nazwisko_lekarza', models.CharField(default='Brak danych', max_length=70)),
                ('id_lekarza', models.IntegerField()),
                ('nr_telefonu', models.CharField(default='Brak danych', max_length=9)),
                ('pwzNumer', models.IntegerField()),
                ('pacjent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.pacjent',default=None)),
                ('rachunek', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.rachunek')),
            ],
        ),
    ]