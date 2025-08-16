from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from user.models import User
from user.serializers import UserReadUpdateSerializer, UserCreateSerializer
from user.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [IsOwnerOrReadOnly()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserReadUpdateSerializer
