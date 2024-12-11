from rest_framework import permissions
from .models import Teachers, Student


class CheckTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        # Проверяем, что user является экземпляром Teacher
        if isinstance(request.user, Teachers):  # Убедитесь, что это преподаватель
            if request.user.user_role == 'teacher':  # Проверка на роль "teacher"
                return True
        return False

class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.created_by:
            return True
        return False

class CheckAssignment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.course.created_by:
            return True
        return False


class CheckTeacherReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'teacher':
            return False
        return True

class CheckReviewOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class CheckStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'student':
            return True
        return False


