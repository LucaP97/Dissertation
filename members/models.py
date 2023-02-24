from django.db import models

class Club(models.Model):
    club_name = models.CharField(max_length=255)
    club_badge = models.ImageField(height_field=None, width_field=None, max_length=100)