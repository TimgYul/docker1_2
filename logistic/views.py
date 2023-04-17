from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

class SearchF(SearchFilter):
    search_param = 'products'
    
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = LimitOffsetPagination
    # при необходимости добавьте параметры фильтрации
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchF]
    search_fields = ['products__title', 'products__description']
