from django.db import models

# Create your models here.

class ContactScheme(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    comment = models.TextField()
  
        
class Post(models.Model):
    text = models.CharField(max_length = 100)

    