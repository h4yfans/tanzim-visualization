from django.views.generic import TemplateView
from django.db.models.functions import Cast
from django.db.models import CharField, DateField

from .models import Vegetable, Product


class IndexView(TemplateView):
    template_name = 'chart/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context['dates'] = list(
            Product.objects.annotate(ndate=Cast('date', CharField())).order_by('date').values_list('ndate', flat=True))
        context['prices'] = list(Product.objects.order_by('date').values_list('price', flat=True))
        return context
