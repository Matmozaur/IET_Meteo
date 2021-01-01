from django.db import models


class City(models.Model):
    """
    class for cities
    """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Weather(models.Model):
    """
    class for weather data entries.
    """
    city = models.CharField(max_length=25)
    time = models.CharField(max_length=25)
    temperature = models.FloatField()
    rain = models.FloatField()
    pressure = models.FloatField()
    wind = models.FloatField()

    @classmethod
    def create(cls, city, time, temperature, rain, pressure, wind):
        weather = cls(city=city, time=time, temperature=temperature, rain=rain, pressure=pressure, wind=wind)
        return weather

    def __str__(self):
        return self.city + ' ' + self.time
