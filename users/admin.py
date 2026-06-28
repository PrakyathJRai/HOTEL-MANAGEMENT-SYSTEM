from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Hospital Information",
            {
                "fields": (
                    "role",
                    "google_access_token",
                    "google_refresh_token",
                    "google_token_expiry",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Hospital Information",
            {
                "fields": ("role",),
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "role",
        "is_staff",
        "is_superuser",
    )