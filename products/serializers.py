from rest_framework import serializers
from .models import Category, Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_primary']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    discount_percentage = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = [
            'id', 'category', 'name', 'slug', 'description', 'price',
            'discount_price', 'discount_percentage', 'stock', 
            'is_featured', 'is_new', 'images', 'created_at'
        ]
    
    def get_discount_percentage(self, obj):
        if obj.discount_price and obj.price > 0:
            discount = ((obj.price - obj.discount_price) / obj.price) * 100
            return int(discount)
        return 0 