import requests
import datetime
import pprint
from datetime import timedelta

from django.utils.dateparse import parse_date

from bs4 import BeautifulSoup

from django.views.generic import TemplateView

from chart.models import Vegetable, Product


class IndexView(TemplateView):
    template_name = 'chart/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        parsed_date = parse_date('2010-01-01')
        today = parse_date('2018-04-07')

        while parsed_date != today:
            data = {
                'tarih': parsed_date,
                'KategoriId00': '6',
                'send00': '1'
            }
            r = requests.post("http://gida.ibb.istanbul/hal-mudurlugu/hal-fiyatlari.html", data=data)
            doc = BeautifulSoup(r._content, 'html.parser')
            doc = doc.find("table", {"class": "tableClass"})
            rows = doc.find_all('tr')
            products = []
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                products.append([ele for ele in cols if ele])
            products.pop(0)

            for item in products:
                low_price = float(item[2][0:-4].replace(',', '.'))
                high_price = float(item[3][0:-4].replace(',', '.'))
                avg_price = (low_price + high_price) / 2
                vegetable, _ = Vegetable.objects.get_or_create(name=item[0])
                vegetable.product_set.create(price=avg_price, unit=item[1], date=parsed_date)

            parsed_date = parsed_date + timedelta(days=1)

            print(parsed_date, len(products))
