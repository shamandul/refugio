from django.urls import path, include

from apps.mascota.views import index


app_name = "mascota"
urlpatterns = [
    path('', index, name="mascota"),
]
