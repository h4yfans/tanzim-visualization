from rest_framework import serializers

from chart.models import Vegetable


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = ('name',)

