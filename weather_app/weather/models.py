from django.db import models

# Create your models here.
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
