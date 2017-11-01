# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.gis import admin
#from django.contrib import admin
from server.models import Farm, House, Well, Crop, Property_house, Property_farm, Identity
# Register your models here.

admin.site.register(House, admin.GeoModelAdmin)
admin.site.register(Identity)
admin.site.register(Farm, admin.GeoModelAdmin)
admin.site.register(Property_house)
admin.site.register(Property_farm)
admin.site.register(Well, admin.GeoModelAdmin)
admin.site.register(Crop)
