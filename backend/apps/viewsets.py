from rest_framework import viewsets

# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class PermissionViewSet(viewsets.ModelViewSet):
    # authentication_classes = (SessionAuthentication, TokenAuthentication)
    authentication_classes = (JWTAuthentication,)
    permission_classes: tuple[type[BasePermission]] = (IsAuthenticated,)
