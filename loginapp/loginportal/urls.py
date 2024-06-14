from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('superuser/', admin.site.urls),
    path('', include("login.urls")),
]
