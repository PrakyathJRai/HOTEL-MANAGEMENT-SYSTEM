from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("doctor", "Doctor"),
        ("patient", "Patient"),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES
    )

    # Google Calendar OAuth Tokens
    google_access_token = models.TextField(
        blank=True,
        null=True
    )

    google_refresh_token = models.TextField(
        blank=True,
        null=True
    )

    google_token_expiry = models.DateTimeField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username