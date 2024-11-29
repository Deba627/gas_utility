"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from requests.views import home  # Assuming you have a 'home' view

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # API URL
    path('api/', include('requests.urls')),

    # Root URL - You can either render a simple homepage or redirect to another page (admin or api)
    path('', home, name='home'),  # Render the homepage view
    # OR you could use this line to redirect root to the admin or api page instead
    # path('', lambda request: redirect('admin/')),  # Uncomment this line to redirect to the admin page
    # path('', lambda request: redirect('api/')),    # Uncomment this line to redirect to the API page
]

