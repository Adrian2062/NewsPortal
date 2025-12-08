from rest_framework import permissions

class IsStaffOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow staff users or the owner of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        # Staff users have full access
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user and request.user.is_staff:
            return True

        # Owners have access
        return obj.user == request.user