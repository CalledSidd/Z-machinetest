from django.urls import path
from . views import UploadView,GetCar,getRoutes

urlpatterns = [
    path('',getRoutes),
    path('retreive',GetCar.as_view({'get':'list'})),
    path('upload',UploadView.as_view())
]
