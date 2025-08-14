from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from user.models import User
from user.serializer import UserSerializer


class UserView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serialized = UserSerializer(user)
        return Response({'user': serialized.data})
