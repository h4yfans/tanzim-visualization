from django.views.generic import TemplateView
from django.db.models.functions import Cast
from django.db.models import CharField

from django.http import JsonResponse

from .models import Vegetable, Product

from .serializers import TanzimSerializer
from rest_framework import viewsets


class IndexView(TemplateView):
    template_name = 'chart/index.html'


class TanzimViewSet(viewsets.ModelViewSet):
    serializer_class = TanzimSerializer
    queryset = Vegetable.objects.all()

    def get_queryset(self):
        qs = super(TanzimViewSet, self).get_queryset()
        qs = qs.objects.get(name='Domates (Pembe)')
        qs = qs.product_set.annotate(ndate=Cast('date', CharField())).order_by('date').qs.values_list('ndate', 'price')

        return qs


def GetIBBData(requests):
    vegetable = Vegetable.objects.get(name='Domates (Pembe)')

    qs = vegetable.product_set.annotate(ndate=Cast('date', CharField())).order_by('date')
    date_and_price = list(qs.values_list('ndate', 'price'))

    import pprint
    pprint.pprint(date_and_price)

    data = {
        'dateandprice': date_and_price,
        'vegetable': vegetable.name
    }

    return JsonResponse(data)
