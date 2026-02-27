from django.contrib import admin

from .models import Event, Mix


@admin.register(Mix)
class MixAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "is_featured", "created_at")
    list_filter = ("is_featured", "genre")
    search_fields = ("title", "description")
    list_editable = ("is_featured",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "venue", "city", "date", "is_upcoming")
    list_filter = ("is_upcoming", "city")
    search_fields = ("title", "venue", "city")
    list_editable = ("is_upcoming",)
