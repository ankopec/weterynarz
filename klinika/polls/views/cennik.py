import csv
from datetime import datetime

from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render

def cennik(request):
    browser = request.headers['User-Agent']

    return render(request, 'cennik.html', {
        'browser': browser,
        'data_zapytania': datetime.now()
    })

def regulamin(request):
    browser = request.headers['User-Agent']

    return render(request, 'regulamin.html', {
        'browser': browser,
        'data_zapytania': datetime.now()
    })

def media(request):
    browser = request.headers['User-Agent']

    return render(request, 'media.html', {
        'browser': browser,
        'data_zapytania': datetime.now()
    })