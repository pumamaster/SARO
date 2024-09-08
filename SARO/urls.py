from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("administrador/", admin.site.urls),
    path("", include('AppSARO.urls')),
]
