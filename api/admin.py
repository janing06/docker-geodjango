from django.contrib import admin
from .models import Barangay
from leaflet.admin import LeafletGeoAdmin


@admin.register(Barangay)
class BarangayAdmin(LeafletGeoAdmin):
     ordering = ['barangay']
