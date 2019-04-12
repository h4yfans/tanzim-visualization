from django.db.models import CharField
from django.db.models.functions import Cast
from rest_framework import serializers

from chart.models import Vegetable, Product


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = ('id', 'name',)

