from django.shortcuts import get_object_or_404
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
from rest_framework import status 

class ProductViewSet(APIView):

    def get_permissions(self):
        if self.request.method in ['GET', 'HEAD', 'OPTIONS']:
            return [AllowAny()]
        else:
            return [IsAdminUser()]

    def get(self, request, slug=None):
        if slug:
            # Retrieve a single product
            product = get_object_or_404(Product, slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        else:
            # List all products with optional filtering and sorting
            max_price = request.GET.get('max_price')
            min_price = request.GET.get('min_price')
            sort = request.GET.get('sort')
            keyword = request.GET.get('keyword')
            products = Product.objects.filter_products(keyword, sort, min_price, max_price)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, slug=None):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug=None):
        product = get_object_or_404(Product, slug=slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RelatedProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, id, *args, **kwargs):
        product_id = id  # request.data.get("product_id")
        print(id)
        if not product_id:
            return Response({"error": "Product Id Not Found"}, status=400)
        product = get_object_or_404(Product, id=product_id)
        products_serialized = ProductSerializer(
            product.get_related_products(), many=True, context={'request': request})
        return Response(products_serialized.data)

    @classmethod
    def get_extra_actions(cls):
        return []
