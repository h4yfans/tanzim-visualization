from django.views.generic import TemplateView
from django.db.models.functions import Cast
from django.db.models import CharField, DateField

from django.http import JsonResponse
import requests

from .models import Vegetable, Product


class IndexView(TemplateView):
    template_name = 'chart/index.html'


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
