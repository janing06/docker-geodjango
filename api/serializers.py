from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Barangay

class BarangaySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Barangay
        fields = '__all__'
        geo_field = 'geom'

        

        