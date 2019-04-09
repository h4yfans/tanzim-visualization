from chart.models import Vegetable
from .serializers import TanzimSerializer
from rest_framework import viewsets


class VegetableViewSet(viewsets.ModelViewSet):
    queryset = Vegetable.objects.all()
    serializer_class = TanzimSerializer
