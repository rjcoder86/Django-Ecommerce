from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product
from.managers import CartManager
User = get_user_model()



class Cart(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    used = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        total = 0
        for item in self.products.all():
            total += int(item.quantity) * float(item.product.price)
        return total

    @property
    def tax_total(self):
        total = 0
        for item in self.products.all():
            total += int(item.quantity) * float(item.product.price) * \
                float(item.product.tax) / 100
        return total

    @property
    def total_cart_products(self):
        return sum(item.quantity for item in self.products.all())


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="products")

    class Meta:
        unique_together = (
            ('product', 'cart')
        )
