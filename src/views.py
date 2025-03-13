from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    return Response({'message': 'Hello, world!'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def send_data_to_csops(request):
    return Response({'message': 'Data sent to HDI', 'data': request.data}, status=status.HTTP_200_OK)
