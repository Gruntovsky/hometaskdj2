from django.core import paginator
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as infile:
        reader = list(csv.DictReader(infile))
        for l in reader:
            Name = l['Name']
            Street = l['Street']
            District = l['District']
            bus_stations = {'Name' : l['Name'],'Street' : l['Street'],'District' : l['District']}
            context = {
                'bus_stations': {'station.Name' : l['Name'],'station.Street' : l['Street'],'station.District' : l['District']}
                # 'page': ...,
            }
    return render(request, 'stations/index.html', context)
