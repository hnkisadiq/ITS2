# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models

# Create your models here.
class Identity(models.Model):
    adhaar_id=models.IntegerField()
    name= models.CharField(max_length=100, blank=True, default='')
    def __str__(self):
        return self.name

class Property_house(models.Model):
    a_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    house_id=models.AutoField(primary_key=True)
    def __str__(self):
        return self.house_id

class Property_farm(models.Model):
    a_id=models.ForeignKey(Identity,on_delete=models.CASCADE)
    farm_id=models.AutoField(primary_key=True)
    def __str__(self):
        return self.farm_id

class House(models.Model):
    h_id=models.ForeignKey(Property_house,on_delete=models.CASCADE)
    h_point = models.PointField(default='')
    area=models.IntegerField()
    income=models.IntegerField()
    img = models.CharField(max_length=500,default='')
    def __str__(self):
        return self.h_id

class Farm(models.Model):
    f_id=models.ForeignKey(Property_farm,on_delete=models.CASCADE)
    area=models.IntegerField()
    poly = models.PolygonField(default='')
    id=models.AutoField(primary_key=True)
    def __str__(self):
        return self.f_id

class Crop(models.Model):
    c_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    output=models.IntegerField()
    farm_id=models.ForeignKey(Farm,on_delete=models.CASCADE)

