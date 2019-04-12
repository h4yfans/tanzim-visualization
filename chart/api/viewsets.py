from rest_framework.response import Response

from chart.models import Vegetable, Product
from .serializers import VegetableSerializer
from rest_framework import viewsets
from django.db.models.functions import Cast
from django.db.models import CharField


class VegetableViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Vegetable.objects.all()
        serializer = VegetableSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        product_id = request.query_params.get('product_id')
        queryset = Product.objects.filter(vegetable_id=product_id).annotate(ndate=Cast('date', CharField())).order_by(
            'date')
        queryset = queryset.values_list('ndate', 'price')
        data = {'data_and_price': queryset}
        return Response(data)
