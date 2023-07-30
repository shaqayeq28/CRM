from django.contrib import admin

from team.models import Team


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_time', 'updated_time', 'is_active']
    readonly_fields = ('created_time', 'updated_time')
    list_filter = ('is_active',)
