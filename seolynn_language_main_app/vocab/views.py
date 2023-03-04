from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import  Response
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    if(request.method == 'GET'):
        return Response({"message": "Some secret"})

class Public(APIView):
    def get(self, request):
        return Response({"message": "Not Secret"})