from django.contrib import admin

from api.models.banner import BannerImage


class ImageAdmin(admin.TabularInline):
    model = BannerImage


class BannerAdmin(admin.ModelAdmin):
    inlines = [
        ImageAdmin,
    ]

    def get_queryset(self, request):
        queryset = super(BannerAdmin, self).get_queryset(request)
        for i, obj in enumerate(queryset):
            if i > 0:
                obj.delete()
        queryset = super(BannerAdmin, self).get_queryset(request)
        return queryset

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
