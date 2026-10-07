from django.db import models

class Meetings(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField(default='9')
    duration = models.IntegerField(default=1)  
