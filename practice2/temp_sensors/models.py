from django.db import models

class TempSensor(models.Model):
    location_id = models.IntegerField()
    last_mesured_date = models.DateField()
    last_mesured_time = models.DateTimeField()
    tempreture = models.CharField(max_length=10)  # can be negative?
    sensor_name = models.CharField(max_length=30)
    sensor_model = models.CharField(max_length=30)
    group_id = models.IntegerField()