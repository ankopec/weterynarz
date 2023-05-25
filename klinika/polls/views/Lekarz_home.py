import csv
from datetime import datetime

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from polls.models import Pacjenci



def lekarz_home(request):
    #browser = request.headers['User-Agent']

    return render(request, 'lekarz/LekarzHome.html')


