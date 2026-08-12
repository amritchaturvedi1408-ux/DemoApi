

from rest_framework import serializers
from .models import User


class SignupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    mobile = serializers.CharField(max_length=15)
    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    def validate_email(self, value):
        value = value.lower()
        if User.objects(email=value).first():
            raise serializers.ValidationError(
                "Email already registered"
            )
        return value

    def validate_mobile(self, value):
        if User.objects(mobile=value).first():
            raise serializers.ValidationError(
                "Mobile number already registered"
            )
        return value