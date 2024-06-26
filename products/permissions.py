from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin can see all orders
        if request.user.is_staff:
            return True
        # User can see their own orders
        return obj.user == request.user
