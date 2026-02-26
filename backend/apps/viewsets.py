from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated


class PermissionViewSet(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes: tuple[type[BasePermission]] = (IsAuthenticated,)
