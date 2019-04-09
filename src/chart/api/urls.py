from django.urls import path
from chart.api.views import TanzimVegetableList

urlpatterns = [
    path('vegetables/', TanzimVegetableList.as_view())
]
