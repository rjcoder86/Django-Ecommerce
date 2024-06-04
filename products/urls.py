from django.urls import path

from .views import ProductViewSet, RelatedProductView

urlpatterns = [
    path("list/", ProductViewSet.as_view()),
    path("add/", ProductViewSet.as_view()),
    path("related/<id>/", RelatedProductView.as_view())
]
