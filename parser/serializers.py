from rest_framework import serializers 
from . models import Car

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class SaveSerialzier(serializers.Serializer):
    class Meta:
        model = Car 
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car 
        fields = '__all__'