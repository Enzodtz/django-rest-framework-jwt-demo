from rest_framework import viewsets
from api.models.banner import Banner
from api.serializers.banner import BannerSerializer


class BannerViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
