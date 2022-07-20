from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="products")
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
