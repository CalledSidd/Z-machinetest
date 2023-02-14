from django.shortcuts import render
from rest_framework import generics
import django_filters 
import io, csv, pandas  
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import filters 
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from . models import Car
from . serializers import UploadSerializer, SaveSerialzier,CarSerializer

# Create your views here.
class UploadView(generics.CreateAPIView):
    serializer_class = UploadSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        read = pandas.read_csv(file)
        for _, row in read.iterrows():
            cars = Car(
                name = row['name'],
                miles_per_gallon = row['mpg'],
                cylinders = row['cyl'],
                displacement = row['disp'],
                horsepower = row['hp'],
                drat = row['drat'],
                weight =row['wt'],
                quarter_mile = row['qsec'],
                configuration = row['vs'],
                transmission = row['am'],
                gears = row['gear'],
                carburetors = row['carb'], 
            )
            cars.save()
        return Response(status=status.HTTP_201_CREATED)

class GetCar(viewsets.ModelViewSet):
    queryset = Car.objects.all()[:50:1]
    serializer_class = CarSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']
