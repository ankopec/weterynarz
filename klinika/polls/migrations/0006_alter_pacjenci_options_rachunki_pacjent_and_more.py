# Generated by Django 4.2.1 on 2023-05-20 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_pacjenci_rachunki_remove_lekarze_pacjent_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacjenci',
            options={'ordering': ['imie_pacjenta', 'nazwisko_własciciela']},
        ),
        migrations.AddField(
            model_name='rachunki',
            name='pacjent',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.pacjenci'),
        ),
        migrations.AddField(
            model_name='rachunki',
            name='podane_leki',
            field=models.CharField(default='Brak danych', max_length=100),
        ),
        migrations.AddField(
            model_name='rachunki',
            name='weterynarz',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.weterynarz'),
        ),
        migrations.AddField(
            model_name='rachunki',
            name='zalecenia',
            field=models.CharField(default='Brak danych', max_length=300),
        ),
        migrations.AlterField(
            model_name='rachunki',
            name='cena_uslugi',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rachunki',
            name='data_wystawienia',
            field=models.DateField(max_length=30),
        ),
    ]
