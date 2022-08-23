from rest_framework.viewsets import ModelViewSet
from product.models import Product
from product.serializers import ProductModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
