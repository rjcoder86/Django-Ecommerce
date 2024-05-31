from django.db import models

class BillingProfileManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter()

