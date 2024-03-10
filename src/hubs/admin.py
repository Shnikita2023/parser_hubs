from django.contrib import admin

from .models import Hub


@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    pass
