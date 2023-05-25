from django.contrib import admin

from .models import Pacjenci
admin.site.register(Pacjenci)

from .models import Rachunek
admin.site.register(Rachunek)

from .models import Weterynarz
admin.site.register(Weterynarz)
# Register your models here.