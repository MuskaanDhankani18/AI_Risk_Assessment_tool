from rest_framework import serializers
from .models import Risk_Assessment

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk_Assessment
        fields = '__all__'
