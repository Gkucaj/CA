from django.db import models

class event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField("Event date:")
    event_venue = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/', blank = True)
    
    def __str__(self):
        return self.event_name


