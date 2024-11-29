from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer, ServiceRequestStatusSerializer


def home(request):
    return HttpResponse("<h1>Welcome to the Gas Utility Service</h1>")

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

    # Custom action to track request status
    @action(detail=True, methods=['get'])
    def track_status(self, request, pk=None):
        request_instance = self.get_object()
        serializer = ServiceRequestStatusSerializer(request_instance)
        return Response(serializer.data)

    # Custom action to resolve the request
    @action(detail=True, methods=['patch'])
    def resolve(self, request, pk=None):
        request_instance = self.get_object()
        request_instance.status = 'resolved'
        request_instance.resolved_at = timezone.now()
        request_instance.save()
        return Response({'status': 'Request resolved'})
