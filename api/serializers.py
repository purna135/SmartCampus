from rest_framework import serializers
from app.models import IrrigationData


class IrrigationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrrigationData
        # fields = ["pump_status"]
        fields = ["pump_status", "ph_level", "moisture_level", "soil_temperature", "nitrogen", "phosphorus", "potassium"]


# class GarbageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Garbage
#         fields = ["bin_id", "garbage_level", "moisture_status", "date"]