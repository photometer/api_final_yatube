from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if obj.author:
            author = obj.author
        else:
            author = obj.user
        if (request.method in permissions.SAFE_METHODS
                or author == request.user):
            return True
        return False
