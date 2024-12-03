from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('item','receiver','sender','pub_time')
    ordering = ('-pub_time',)

admin.site.register(Message, MessageAdmin)
