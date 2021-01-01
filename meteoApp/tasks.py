from __future__ import absolute_import, unicode_literals
import requests
from celery import shared_task
from meteoApp.models import Weather, City


@shared_task
def download_data():
    """
    Function for updating database regularly.
    """
    url = 'https://danepubliczne.imgw.pl/api/data/synop/station/{}'
    cities = City.objects.all()
    for city in cities:
        r = requests.get(url.format(city)).json()
        if len(r['godzina_pomiaru']) == 1:
            r['godzina_pomiaru'] = '0' + str(r['godzina_pomiaru'])
        city_weather = {
            'city': city.name,
            'time': r['data_pomiaru']+ ' ' + r['godzina_pomiaru'],
            'temperature': float(r['temperatura']),
            'rain': float(r['suma_opadu']),
            'pressure': float(r['cisnienie']),
            'wind': float(r['predkosc_wiatru']),

        }
        weather = Weather.create(**city_weather)
        weather.save()



