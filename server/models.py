# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class Identity(models.Model):
    adhaar_id=models.IntegerField()
    name= models.CharField(max_length=100, blank=True, default='')

class Property_house(models.Model):
    a_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    house_id=models.AutoField(primary_key=True)

class Property_farm(models.Model):
    a_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    farm_id=models.AutoField(primary_key=True)

class House(models.Model):
    h_id=models.ForeignKey(Property_house,on_delete=models.CASCADE)
    h_point = models.PointField(default='')
    area=models.IntegerField()
    income=models.IntegerField()
    img = models.FileField(default='')

class Farm(models.Model):
    f_id=models.ForeignKey(Property_farm,on_delete=models.CASCADE)
    area=models.IntegerField()
    poly = models.PolygonField(default='')

class Crop(models.Model):
    c_id=models.ForeignKey(Farm,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    output=models.IntegerField()
    year = models.IntegerField()
class Well(models.Model):
    w_id=models.AutoField(primary_key=True)
    w_point = models.PointField(default='')
    depth=models.IntegerField()
    year = models.IntegerField()
