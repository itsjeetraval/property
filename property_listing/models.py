from django.db import models


class PropertyListing(models.Model):
 
  
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)

    property_type = models.CharField(max_length=50, choices=[
        ('Residential','Residential'),
        ('Commercial','Commercial'),
        ('Villa','Villa')
    ])

    status = models.CharField(max_length=20,choices=[
        ('Available','Available'),
        ('Sold','Sold')
    ])


   

