from wsgiref.validate import validator
from rest_framework import serializers
from api.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ("image",)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = "__all__"
