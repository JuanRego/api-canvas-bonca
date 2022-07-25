from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from .models import Canvas
from .serializers import CanvasSerializer

class ListCreateCanvasView(generics.ListCreateAPIView):
  queryset = Canvas.objects.all()
  serializer_class = CanvasSerializer

class RetrieveUpdateDestroyCanvasView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Canvas.objects.all()
  serializer_class = CanvasSerializer

  lookup_url_kwarg = "canvas_id"

class GetTheCanva(APIView):
    # authentication_classes = [TokenAuthentication]
    
    def get(self, request):
        theCanvaid = Canvas.objects.filter(name='thecanva')
        
        print(theCanvaid)
        
        theCanva = theCanvaid[0]
        
        context = theCanva.reference
        
        return Response({
        'context': str(context),
        })
    