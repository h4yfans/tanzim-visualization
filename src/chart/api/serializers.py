from rest_framework import serializers

from chart.models import Vegetable, Product


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = ('id', 'name',)


class ProductSerializer(serializers.Serializer):
    date_and_price = serializers.DictField()
