from django.db import models
from django.db.models.functions import Length

from app import settings

models.CharField.register_lookup(Length)
models.TextField.register_lookup(Length)


class Card(models.Model):
    """List of prices
    Is used also for populating user's online store
    as well as is shown on catalog,
    user can use multiple addition
    """
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(name__length__gte=5),
                name="Card's_name_min_length",
            )
        ]

    def __str__(self):
        return self.name


class Ad(models.Model):
    """Announcements
    are shown only on urls of marketplace,
    can't be added new. Just old ads.
    """
    name = models.CharField(max_length=70)
    description = models.TextField()
    phone = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    cities = models.ForeignKey("City", on_delete=models.SET_NULL, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(name__length__gte=10),
                name="Ad's_name_min_length",
            ),
            models.CheckConstraint(
                check=models.Q(description__length__gte=30),
                name="Ad's_description_min_length",
            )
        ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=120)
    cards = models.ManyToManyField(Card, related_name="cities")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
