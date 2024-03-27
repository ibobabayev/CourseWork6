from django.contrib import admin
from services.models import *

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('fio','email',)
    search_fields = ('fio',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject','body',)
    search_fields = ('body',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('status','periodicity',)
    list_filter = ('status','periodicity',)

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('attempt','attempt_time','response',)
    search_fields = ('client','newsletter',)