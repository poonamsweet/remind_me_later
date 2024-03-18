from django.contrib import admin
from .models import Reminder
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class ReminderAdmin(BaseUserAdmin):

    list_display = ["id", "user", "date", "time", "message"]
    list_filter = ["date"]
    fieldsets = [
        (None, {"fields": ["user", "date", "time", "message", "reminder_type"]}),

    ]
    search_fields = ["date"]
    ordering = ["-id"]
    filter_horizontal = []


admin.site.register(Reminder, ReminderAdmin)
