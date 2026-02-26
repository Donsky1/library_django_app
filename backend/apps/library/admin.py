from django.contrib import admin

from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year", "is_deleted")
    list_select_related = ("author",)
    list_filter = ("author",)
    search_fields = ("title", "author__first_name", "author__last_name")


@admin.register(models.Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "duration_at", "created_at", "returned_at")
    list_select_related = ("user", "book")
    list_filter = ("user__email", "book__title", "book__author__first_name", "book__author__last_name")
    autocomplete_fields = ("user", "book")


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "date_of_birth", "is_deleted")
    search_fields = ("first_name", "last_name")
