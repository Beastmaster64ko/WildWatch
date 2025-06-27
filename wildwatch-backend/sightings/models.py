from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Sighting(models.Model):
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='sightings_images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

