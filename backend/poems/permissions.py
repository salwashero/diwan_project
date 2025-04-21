# backend/poems/permissions.py

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    صلاحية مخصصة للسماح لملاك الكائن فقط بتعديله أو حذفه.
    الآخرون يمكنهم القراءة فقط.
    """

    def has_object_permission(self, request, view, obj):
        """
        يتم استدعاؤها عند الوصول إلى كائن معين (مثل قصيدة واحدة).
        """
        # صلاحيات القراءة (GET, HEAD, OPTIONS) مسموحة لأي طلب.
        if request.method in permissions.SAFE_METHODS:
            return True

        # صلاحيات الكتابة (PUT, PATCH, DELETE) مسموحة فقط إذا كان
        # المستخدم الذي أرسل الطلب (request.user) هو نفسه مالك الكائن (obj.owner).
        # نفترض أن النموذج (obj) لديه حقل اسمه 'owner'.
        return obj.owner == request.user
