import requests
from django.shortcuts import render

from .draw import draw, draw_wth_trend, draw_stats
from .models import City, Weather
from .forms import CityForm


context = dict()


def index(request):
    url = 'https://danepubliczne.imgw.pl/api/data/synop/station/{}'
    if request.method == 'POST':
        form = CityForm(request.POST)
        r = requests.get(url.format(request.POST['name'])).json()
        if r.get('temperatura', False):
            form.save()
        else:
            pass
    form = CityForm()
    cities = City.objects.all()
    context['form'] = form
    context['cities'] = list(cities)
    context['selected_city'] = 'krakow'
    context['measurement'] = 'temperature'
    context['time'] = 'day'
    context['stats'] = 'Statistics'
    draw(context['selected_city'], context['measurement'], context['time'])
    return render(request, 'meteoApp/meteoApp.html', context)


def basic_plot(request):
    if request.method == 'POST':
        context['selected_city'] = request.POST.get("city")
        context['measurement'] = request.POST.get("measurement")
        context['time'] = request.POST.get("time")
    context['stats'] = 'Statistics'
    draw(context['selected_city'], context['measurement'], context['time'])
    return render(request, 'meteoApp/meteoApp.html', context)


def add_trend(request):
    if request.method == 'POST':
        draw_wth_trend(context['selected_city'], context['measurement'], context['time'])
    return render(request, 'meteoApp/meteoApp.html', context)


def add_stats(request):
    if request.method == 'POST':
        context['stats'] = draw_stats(context['selected_city'], context['measurement'], context['time'])
    return render(request, 'meteoApp/meteoApp.html', context)