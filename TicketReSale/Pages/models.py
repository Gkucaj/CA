from django.db import models
from django.conf import settings




class event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField("Event date:")
    event_venue = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='images/', blank = True)
    
    def __str__(self):
        return self.event_name



class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
       return self.title 



class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    def __str__(self):
       return self.title 


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE)
    items= models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)

    def __str__(self):
       return self.title 