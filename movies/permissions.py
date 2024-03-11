from rest_framework.permissions import BasePermission


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return (
            request.method == "GET"
            or request.user.is_authenticated
            and request.user.is_employee
        )
