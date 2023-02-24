from django.db import models

class Club(models.Model):
    club_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    country = models.CharField(max_length=255)
    founded = models.DateField()
    national = models.BooleanField()
    logo = models.ImageField(height_field=None, width_field=None, max_length=100)

class Venue(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    venue_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    capacity = models.IntegerField()
    surface = models.CharField(max_length=255)
    image = models.ImageField()
