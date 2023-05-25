# Generated by Django 4.2.1 on 2023-05-22 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_pacjent_imie_własciciela'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rachunek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_wystawienia', models.DateField(max_length=30)),
                ('cena_uslugi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diagnoza', models.CharField(max_length=500)),
                ('podane_leki', models.CharField(default='Brak danych', max_length=100)),
                ('zalecenia', models.CharField(default='Brak danych', max_length=300)),
                ('pacjenci', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.pacjenci')),
                ('weterynarz', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.weterynarz')),
            ],
        ),
    ]
