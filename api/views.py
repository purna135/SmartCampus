from rest_framework.response import Response
from rest_framework.decorators import api_view
from app.models import IrrigationData
from .serializers import IrrigationDataSerializer
from django.http import JsonResponse


@api_view(["POST", "GET"])
def add_irrigation_data(request):
    if request.method == "GET":
        serializer = IrrigationDataSerializer(data = request.GET)
    else:
        serializer = IrrigationDataSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
