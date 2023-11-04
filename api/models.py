from django.db import models
from django.contrib.gis.db import models as gis_models

class Barangay(models.Model):
    barangay = models.CharField(max_length=80)
    code = models.CharField(max_length=80, unique=True)
    municipal = models.CharField(max_length=80)
    longitude = models.FloatField()
    latitude = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)
    
    def __str__(self):
        return self.barangay
