from rest_framework import serializers
from .models import Patient


class PatientSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.DateTimeField()
    gender = serializers.CharField()
    
    def create(self, validated_data):
        return Patient.objects.create(**validated_data)
