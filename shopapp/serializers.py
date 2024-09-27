from rest_framework import serializers
from .models import Product, Order, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'discount','archived', 'images']

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ['id', 'delivery_address','created_at', 'user', 'products']
