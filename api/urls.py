from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from api.views import *

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"products", ProductViewSet)
router.register(r"banners", BannerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", CustomTokenObtainPairView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
    path("auth/verify/", TokenVerifyView.as_view()),
]
