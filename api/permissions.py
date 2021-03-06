from rest_framework.permissions import BasePermission, SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allows users to update their own profile"""

    def has_object_permission(self, request, view, obj):
        """Checks if user is trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(BasePermission):
    """Allows users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Checks if user is trying to edit their own status"""
        if request.method in SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
