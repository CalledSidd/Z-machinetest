from django.urls import path
from . views import UploadView,GetCar

urlpatterns = [
    path('retreive',GetCar.as_view({'get':'list'})),
    path('upload',UploadView.as_view())
]
