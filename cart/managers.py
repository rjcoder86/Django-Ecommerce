from django.db import models

class CartManager(models.Manager):
    def get_existing_or_new(self, request):
        created = False
        cart_id = request.session.get('cart_id')
        if self.get_queryset().filter(id=cart_id, used=False).count() == 1:
            obj = self.model.objects.get(id=cart_id)
        elif self.get_queryset().filter(user=request.user, used=False).count() == 1:
            obj = self.model.objects.get(user=request.user, used=False)
            request.session['cart_id'] = obj.id
        else:
            obj = self.model.objects.create(user=request.user)
            request.session['cart_id'] = obj.id
            created = True
        return obj, created