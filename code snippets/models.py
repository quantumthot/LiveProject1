from django.db import models


# Create your models here.
class Entry(models.Model):
    resort = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    tickets = models.CharField(max_length=50, default='')
    date = models.CharField(max_length=50)
    conditions = models.TextField(max_length=1000)
    # Model manager
    Entries = models.Manager()

    def __str__(self):
        return self.resort


class WeatherMoment(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    WeatherMoments = models.Manager()

    def __str__(self):
        return self.date
