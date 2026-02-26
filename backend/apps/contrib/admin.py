from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    search_fields = ("uuid", "email", "first_name", "last_name")
    ordering = ("-date_joined",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Персональная информация",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "groups",
                )
            },
        ),
        (
            "Права доступа",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (
            "Важные даты",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        else:
            return (
                (
                    None,
                    {
                        "fields": (
                            "email",
                            "password",
                        )
                    },
                ),
                (
                    "Персональная информация",
                    {
                        "fields": (
                            "first_name",
                            "last_name",
                            "groups",
                        )
                    },
                ),
                (
                    "Права доступа",
                    {
                        "fields": (
                            "is_active",
                            "is_staff",
                        ),
                    },
                ),
                (
                    "Важные даты",
                    {
                        "fields": (
                            "last_login",
                            "date_joined",
                        )
                    },
                ),
            )
