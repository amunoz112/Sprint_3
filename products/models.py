from django.db import models

class Product(models.Model):
    sku = models.CharField(max_length=64, unique=True)         # código único
    name = models.CharField(max_length=255)                    # nombre del producto
    quantity_available = models.PositiveIntegerField(default=0)  # cantidad en stock
    is_active = models.BooleanField(default=True)              # activo / inactivo

    def __str__(self):
        return f"{self.sku} - {self.name}"
