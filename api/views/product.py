from rest_framework import viewsets
from api.models.product import Product
from api.serializers.product import ProductSerializer
from rest_framework import filters


class ProductViewSet(viewsets.ModelViewSet):
    search_fields = ["name"]
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
