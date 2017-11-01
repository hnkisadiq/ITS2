from django.conf.urls import url
from server import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^identity/$', views.identity_list),
    url(r'^property_house/$', views.property_house_list),
    url(r'^property_farm/$', views.property_farm_list),
    url(r'^house/$', views.house_list),
    url(r'^farm/$', views.farm_list),
    url(r'^crop/$', views.crop_list),
    url(r'^well/$', views.well_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
