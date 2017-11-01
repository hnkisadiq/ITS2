from rest_framework import serializers
from server.models import Farm, Well, House, Identity, Property_house, Property_farm, Crop

class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity
        fields = '_all__'
class Property_houseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_house
        fields = '__all__'

class Property_farmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property_farm
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'
class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'
class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'
class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'
