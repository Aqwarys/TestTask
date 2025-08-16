from rest_framework import serializers

from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Order
        fields = ['id', 'name', 'description', 'created_at', 'user']

        read_only_fields = ['created_at', 'user']