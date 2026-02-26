from rest_framework import viewsets

from apps.library.api.v1.serializers import (
    AuthorSerializer,
    BookSerializer,
)
from apps.library.models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.filter(is_deleted=False)
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.filter(is_deleted=False)
    serializer_class = BookSerializer
