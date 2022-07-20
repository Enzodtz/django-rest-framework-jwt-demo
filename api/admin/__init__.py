from django.contrib import admin
from api.models import *
from .product import *
from .banner import *

# Register your models here.

admin.site.register(User)
# admin.site.register(Product)
# admin.site.register(Image)
admin.site.register(Product, ProductAdmin)
admin.site.register(Banner, BannerAdmin)
