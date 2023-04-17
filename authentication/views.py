from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from authentication.models import User
from authentication.serializers import UserCreateSerialize


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerialize
