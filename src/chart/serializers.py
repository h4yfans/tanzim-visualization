from rest_framework import serializers

from .models import Vegetable


class TanzimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = ('name',)

