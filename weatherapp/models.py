from django.db import models

# Create your models here.


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    coordinate = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add= True)