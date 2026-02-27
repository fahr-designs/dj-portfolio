from django.db import models


class Mix(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_url = models.URLField(blank=True)
    cover_image = models.ImageField(upload_to="mixes/", blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True)
    duration = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Mix"
        verbose_name_plural = "Mixes"

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    ticket_url = models.URLField(blank=True)
    is_upcoming = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"{self.title} @ {self.venue}"
