from django.db import models
from django.contrib.gis.db import models as geomodels

from django_google_maps import fields as map_fields


class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name',)

        # plural form in admin view
        verbose_name_plural = 'cities'
