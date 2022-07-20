from wsgiref.validate import validator
from rest_framework import serializers
from api.models import BannerImage, Banner


class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = ("image",)


class BannerSerializer(serializers.ModelSerializer):
    images = BannerImageSerializer(read_only=True, many=True)

    class Meta:
        model = Banner
        fields = ["id", "images"]
