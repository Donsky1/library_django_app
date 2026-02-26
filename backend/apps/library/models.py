from config import settings
from django.db import models

from apps.contrib.models import HistoryModel, SoftDeleteMixin


class Author(HistoryModel, SoftDeleteMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        db_table = "author"
        ordering = ("last_name", "first_name")


class Book(HistoryModel, SoftDeleteMixin):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} ({self.author.last_name}. {self.author.first_name})"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "book"
        ordering = ("title",)


class Loan(HistoryModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")

    duration_at = models.IntegerField(default=14)
    returned_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}: <{self.book}>"

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        db_table = "loan"
