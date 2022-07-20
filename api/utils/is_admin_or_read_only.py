from rest_framework import permissions

SAFE_METHODS = ["GET", "HEAD", "OPTIONS"]


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        if (
            request.method in SAFE_METHODS
            or request.user
            and request.user.is_authenticated()
        ):
            return True
        return False
