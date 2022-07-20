from django.contrib import admin

from api.models.product import ProductImage, Product


class ImageAdmin(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin,
    ]
