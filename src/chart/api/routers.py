from chart.api.viewsets import VegetableViewSet, ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('vegetables', VegetableViewSet, base_name='vegetable')
router.register('products', ProductViewSet, base_name='products')

