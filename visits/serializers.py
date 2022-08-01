from rest_framework import serializers
from .models import Visit, VisitDetails


DECIMAL_FIELDS_KWARGS = {
    'max_digits': 10,
    'decimal_places': 1,
    'default': 0.0,
}


class VisitSerializer(serializers.Serializer):
    patient = serializers.CharField()
    visit_date = serializers.DateTimeField()
    height = serializers.DecimalField(**DECIMAL_FIELDS_KWARGS)
    weight = serializers.DecimalField(**DECIMAL_FIELDS_KWARGS)
    BMI = serializers.DecimalField(**DECIMAL_FIELDS_KWARGS)
    
    class Meta:
        model = Visit
        fields = '__all__'
    
    def create(self, validated_data):
        return Visit.objects.create(**validated_data)


class VisitDetailsSerializer(serializers.Serializer):
    visit = serializers.CharField()
    general_health_status = serializers.CharField()
    health_question = serializers.CharField()
    comments = serializers.CharField()

    class Meta:
        model = VisitDetails
        fields = '__all__'
    
    def create(self, validated_data):
        return VisitDetails.objects.create(**validated_data)
