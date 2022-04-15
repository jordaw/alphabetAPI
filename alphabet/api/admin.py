from django.contrib import admin

from .models import History


class HistoryAdmin(admin.ModelAdmin):
    """Configures django admin to show important information.
    
    Accessible at localhost:8000/admin/ (after superuser created).
    """
    fieldsets = [
        ("Request", {"fields": ["request"]}),
        ("Response", {"fields": ["response"]}),
        ("Created", {"fields": ["created"]}),
    ]

    readonly_fields = ["created"]

    list_display = ("request", "response")

admin.site.register(History, HistoryAdmin)

admin.site.site_header = "AlphabetAPI Admin Panel"