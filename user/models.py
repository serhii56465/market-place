from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    money = models.FloatField(null=True, blank=True, default=0.0)
    rating = models.IntegerField(null=True, blank=True, default=0.0)

    class Meta:
        ordering = ["date_joined"]
