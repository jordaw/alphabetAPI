"""api URL dispatcher/configuration
    
Registers API application routes
"""

from django.urls import path

from . import views


urlpatterns = [
    path('check', views.AlphabetAPIView.as_view()),
]