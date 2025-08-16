from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions

from order.models import Order
from order.serializers import OrderSerializer
from user.models import User


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
