from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import SignupSerializer
from .utils import hash_password, verify_password
from .token import create_tokens

# Create your views here.
class SignupAPIView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        data = serializer.validated_data
        user = User(
            name=data["name"],
            email=data["email"],
            mobile=data["mobile"],
            password=hash_password(data["password"])
        )
        user.save()
        tokens = create_tokens(user)
        return Response(
            {
                "message": "Signup successful",
                "user": {
                    "id": str(user.id),
                    "name": user.name,
                    "email": user.email,
                    "mobile": user.mobile
                },
                "tokens": tokens
            },
            status=status.HTTP_201_CREATED
        )



class LoginAPIView(APIView):
    def post(self, request):
        login = request.data.get("login")
        password = request.data.get("password")
        if not login or not password:
            return Response(
                {
                    "message": "Login and password are required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects(
            email=login.lower()
        ).first()

        if not user:
            user = User.objects(
                mobile=login
            ).first()

        if not user:

            return Response(
                {
                    "message": "Invalid email/mobile or password"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not verify_password(
            password,
            user.password
        ):

            return Response(
                {
                    "message": "Invalid email/mobile or password"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not user.is_active:

            return Response(
                {
                    "message": "Account is inactive"
                },
                status=status.HTTP_403_FORBIDDEN
            )

        tokens = create_tokens(user)

        return Response(
            {
                "message": "Login successful",

                "user": {
                    "id": str(user.id),
                    "name": user.name,
                    "email": user.email,
                    "mobile": user.mobile
                },

                "tokens": tokens
            },
            status=status.HTTP_200_OK
        )
