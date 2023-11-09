from rest_framework import serializers
from main.models import CarPass

class CarPassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPass
        fields = ('brand', 'model', 'plate_number', 'owners_name')