from django.db import models
from django.db.models import Q

class ProductManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def filter_products(self, keyword, sort, min_price, max_price):
        qs = self.get_queryset().filter(active=True)
        if keyword:
            qs = qs.filter(
                Q(tag_list__title__icontains=keyword) |
                Q(title__icontains=keyword)
            ).distinct()
        if sort:
            sort = int(sort)
            if sort == 2:
                qs = qs.order_by('-price')
            elif sort == 1:
                qs = qs.order_by('price')
        if max_price:
            max_price = int(max_price)
            qs = qs.filter(price__lt=max_price)
        if min_price:
            min_price = int(min_price)
            qs = qs.filter(price__gt=min_price)
        return qs

    def get_products(self):
        return self.get_queryset().filter(active=True)

