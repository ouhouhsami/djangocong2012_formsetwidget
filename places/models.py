from django.db import models

class PlaceType(models.Model):
    """
    Type of place
    """
    label = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Place(models.Model):
    """
    Place, more ore less point of interest on a map, 
    with relation to placetype

    For mock-up purpose, we don't use django GIS possibilities
    """
    place_type = models.ForeignKey(PlaceType)
    title = models.CharField(max_length=255)
    comment = models.TextField(blank=True)
    position = models.CharField(max_length=255)