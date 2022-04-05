from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name')
    list_fields = ('email', 'name')


admin.site.register(UserProfile, UserProfileAdmin)
