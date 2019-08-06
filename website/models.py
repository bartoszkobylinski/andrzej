from django.db import models
from osm_field.fields import LatitudeField, LongitudeField, OSMField

# Create your models here.

class ContactScheme(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    comment = models.TextField()
  
        
class Post(models.Model):
    text = models.CharField(max_length = 100)

class MyMap(models.Model):
    location = OSMField(lat_field = 'latitude',lon_field = 'longitude')
    latitude = LatitudeField()
    longitude = LongitudeField()