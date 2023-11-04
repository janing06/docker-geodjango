from django.urls import path,include
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'barangays', views.BarangayViewSet)

urlpatterns = [
     path('', views.index, name='index'),
     path('api/', include(router.urls)),
     path('barangay/', views.AllBarangayGeoJSONView.as_view(), name='all-barangay'),
     path('barangay/<str:code>/', views.SingleBarangayGeoJSONView.as_view(), name='single-barangay'),
]