from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    RATING_CHOICES = {
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    }

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="movies"
    )
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default="", blank=True)
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default="G")
    synopsis = models.TextField(default="", blank=True)
