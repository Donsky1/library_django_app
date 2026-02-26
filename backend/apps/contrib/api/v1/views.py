from rest_framework import viewsets

from apps.contrib.api.v1.serializers import UserDetailSerializer, UserSerializer
from apps.contrib.models import User
from apps.viewsets import PermissionViewSet


class UserViewSet(PermissionViewSet, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return super().get_serializer_class()
