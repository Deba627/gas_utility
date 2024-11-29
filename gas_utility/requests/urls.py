from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceRequestViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'requests', ServiceRequestViewSet)  # Register the ServiceRequest API endpoint

urlpatterns = [
    path('', include(router.urls)),  # Include all the routes from the router
]
