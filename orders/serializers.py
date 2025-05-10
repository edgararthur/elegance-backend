from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'price', 'quantity', 'total_price']
    
    def get_total_price(self, obj):
        return obj.get_cost()

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_cost = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'first_name', 'last_name', 'email', 
            'address', 'postal_code', 'city', 'status', 'status_display',
            'created_at', 'updated_at', 'items', 'total_cost'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']
    
    def get_total_cost(self, obj):
        return obj.get_total_cost() 