from user.models import User
from rest_framework import serializers


class UserReadUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'age',
        ]

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'age', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user