from django.db import models

# Create your models here.
class Gallerymodel(models.Model):
    ShelterCode = models.CharField(max_length=255,)
    Organization = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    UserName = models.CharField(max_length=255)
    MajorTasks = models.CharField(max_length=255)
    Tasks = models.CharField(max_length=255)
    Latitude = models.FloatField()
    Longitude =models.FloatField()
    SubDate = models.DateField()
    Comments = models.CharField(max_length=1000)
    Image1 = models.CharField(max_length=255)
    Image1Caption = models.CharField(max_length=255)
    Image2 = models.CharField(max_length=255)
    Image2Caption = models.CharField(max_length=255)
    Image3 = models.CharField(max_length=255)
    Image3Caption = models.CharField(max_length=255)
    Image4 = models.CharField(max_length=255)
    Image4Caption = models.CharField(max_length=255)
    Image5 = models.CharField(max_length=255)
    Image5Caption = models.CharField(max_length=255)
