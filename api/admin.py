from django.contrib import admin
from .models import UserProfile, ProfileFeedItem


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name')
    list_filter = ('email', 'name')


class ProfileFeedItemAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'status_text', 'created_on')
    search_fields = ('user_profile', 'status_text')
    list_filter = ('user_profile', 'status_text')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)
