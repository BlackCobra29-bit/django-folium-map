from django.contrib import admin
from django.urls import path
from App.views import Folium_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Folium_map, name = "folium-map")
]