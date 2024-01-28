
from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp')
    search_fields = ('message',)
    # Add any other configurations you want for the admin interface
