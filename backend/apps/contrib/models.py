from uuid import uuid4

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from apps.contrib import managers


class User(AbstractUser):
    username = None
    uuid = models.UUIDField(verbose_name="UUID", primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(verbose_name="E-mail", unique=True)
    first_name = models.CharField(verbose_name="Имя", max_length=32)
    last_name = models.CharField(verbose_name="Фамилия", max_length=32)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = managers.UserManager()
    groups = models.ManyToManyField(
        Group,
        verbose_name="Группы",
        related_name="custom_user_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="Разрешения пользователя",
        related_name="custom_user_permissions",
        blank=True,
    )

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Системные пользователи"
        db_table = "core_user"
        ordering = ("-date_joined",)

    def __str__(self):
        return self.email

    @property
    def full_name(self) -> str:
        return f"{self.last_name} {self.first_name}".strip()

    @property
    def short_name(self) -> str:
        return f"{self.last_name} {str(self.first_name)[0]}.".strip()

    def get_full_name(self) -> str:
        return self.full_name

    def get_short_name(self) -> str:
        return self.short_name


class HistoryModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
