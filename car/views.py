from django.shortcuts import render
from . models import Car
from .serializers import CarSerializer
from rest_framework import generics
# Create your views here.

class CarApiList(generics.ListAPIView):
    serializer_class = CarSerializer
    def get_queryset(self):
        return Car.objects.prefetch_related('details').prefetch_related('details__detail_type').prefetch_related('details__extras').all()

def car_template_list(request):
        cars = Car.objects.prefetch_related('details').prefetch_related('details__detail_type').prefetch_related('details__extras').all()
        return render(request, 'car/list.html', {'cars': cars})
        
