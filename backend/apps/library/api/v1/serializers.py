from rest_framework import serializers

from apps.library.models import Author, Book, Loan


class AuthorSerializer(serializers.ModelSerializer[Author]):
    url = serializers.HyperlinkedIdentityField(view_name="author-detail")

    class Meta:
        model = Author
        fields = (
            "url",
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "url")


class BookSerializer(serializers.ModelSerializer[Author]):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "author",
            "publication_year",
            "description",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")


class LoanSerializer(serializers.ModelSerializer[Loan]):
    class Meta:
        model = Loan
        fields = (
            "id",
            "user",
            "book",
            "duration_at",
            "returned_at",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "duration_at")
