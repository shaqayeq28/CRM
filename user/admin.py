from django.contrib import admin

# Register your models here.
from user.models import UserProfile, Lead, Client


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time', 'updated_time', 'is_active']
    readonly_fields = ('created_time', 'updated_time')
    list_filter = ('is_active',)


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'priority', 'created_by', 'status', 'description', 'created_time', 'updated_time',
                    'is_active']
    list_filter = ('priority', 'status', 'is_active')
    raw_id_fields = ('created_by',)
    readonly_fields = ('created_time', 'updated_time')


@admin.register(Client)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_by', 'description', 'created_time', 'updated_time', 'is_active']
    list_filter = ('is_active',)
    raw_id_fields = ('created_by',)
    readonly_fields = ('created_time', 'updated_time')
