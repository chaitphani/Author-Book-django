from django.contrib import admin
from django.urls import path, include

import authApp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authApp.urls')),
]
