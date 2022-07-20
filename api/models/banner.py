from django.db import models


class Banner(models.Model):
    def __str__(self):
        return "Banner"


class BannerImage(models.Model):
    image = models.ImageField(upload_to="banners")
    banner = models.ForeignKey(Banner, related_name="images", on_delete=models.CASCADE)
