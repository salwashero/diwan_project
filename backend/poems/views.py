# backend/poems/views.py

from rest_framework import viewsets, permissions
from .models import Poem
from .serializers import PoemSerializer
from .permissions import IsOwnerOrReadOnly  # <<< تأكد من أنه غير معلق


class PoemViewSet(viewsets.ModelViewSet):
    """
    ViewSet يوفر نقاط نهاية CRUD لنموذج Poem.
    يضمن تعيين المالك تلقائيًا عند الإنشاء.
    يطبق صلاحيات المالك للقراءة فقط.
    """

    queryset = Poem.objects.all().order_by("-created_at")
    serializer_class = PoemSerializer
    # --- تطبيق الصلاحيات ---
    # الآن: المسجل دخوله يقرأ ويكتب، والمالك فقط يعدل/يحذف قصائده
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]  # <<< تم التعديل هنا

    def perform_create(self, serializer):
        """تعيين المستخدم الحالي كمالك للقصيدة عند إنشائها."""
        serializer.save(owner=self.request.user)
