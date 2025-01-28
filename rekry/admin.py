from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    search_fields = ('title', 'location')
    list_filter = ('location',)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'job__title')
    list_filter = ('job',)
