# myapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Calculation
from .serializers import CalculationSerializer

@api_view(['POST'])
def add_numbers(request):
    operand1 = request.data.get('operand1', 0)
    operand2 = request.data.get('operand2', 0)
    result = operand1 + operand2

    calculation = Calculation.objects.create(operand1=operand1, operand2=operand2, result=result)
    serializer = CalculationSerializer(calculation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_all_data(request):
    calculations = Calculation.objects.all()
    serializer = CalculationSerializer(calculations, many=True)
    return Response(serializer.data)
