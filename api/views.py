from django.shortcuts import render
from .serializers import BarangaySerializer
from rest_framework.views import APIView
from .models import Barangay
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
import json
from django.core.serializers import serialize


class BarangayViewSet(viewsets.ModelViewSet):
    queryset = Barangay.objects.all().order_by('barangay')
    serializer_class = BarangaySerializer


def index(request):
    
    barangays = Barangay.objects.all().order_by('barangay')
    serializer = BarangaySerializer(barangays, many=True)
    
    geojson_data = serialize('geojson', Barangay.objects.all(), geometry_field='geom', fields=('code'))    
    
    print(geojson_data)
    
    return render(request, 'api/index.html',{'data': json.dumps(geojson_data)})
 
 
class SingleBarangayGeoJSONView(APIView):
    def get(self, request, code):
        barangay = get_object_or_404(Barangay, code=code)
        serializer = BarangaySerializer(barangay)
        return Response(serializer.data)


class AllBarangayGeoJSONView(APIView):
    def get(self, request):
        barangays = Barangay.objects.order_by('barangay')
        serializer = BarangaySerializer(barangays, many=True)   
        return Response(serializer.data)
    
    

   

          
