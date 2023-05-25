import csv
from datetime import datetime

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render

def home(request):
    browser = request.headers['User-Agent']

    return render(request, 'home.html', {
        'browser': browser,
        'data_zapytania': datetime.now()
    })