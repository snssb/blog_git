from rest_framework import permissions



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.method, 'req')
        if request.method in permissions.SAFE_METHODS and request.method is not 'PATCH':
            return True

        return obj.author_l == request.user
