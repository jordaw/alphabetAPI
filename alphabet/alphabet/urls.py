"""alphabet URL dispatcher/configuration

Registers API application routes
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # includes all urls in api application urls.py
    path('api/alphabet/', include('api.urls')),
]
