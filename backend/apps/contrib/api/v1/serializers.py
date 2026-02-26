from rest_framework import serializers

from apps.contrib import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("uuid", "email", "first_name", "last_name")


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        exclude = ("password",)
