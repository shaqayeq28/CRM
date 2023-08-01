from django.contrib import admin

from team.models import Team, TeamPlan


# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'plan', 'created_by', 'created_time', 'updated_time', 'is_active']
    readonly_fields = ('created_time', 'updated_time')
    list_filter = ('is_active',)


@admin.register(TeamPlan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'max_leads', 'max_clients', 'description', 'created_time', 'updated_time',
                    'is_active']
    readonly_fields = ('created_time', 'updated_time')
    list_filter = ('is_active',)
