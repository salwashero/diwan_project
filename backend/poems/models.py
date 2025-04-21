# backend/poems/models.py

from django.db import models
from django.conf import settings  # <<< تم إلغاء التعليق


class Poem(models.Model):
    title = models.CharField(max_length=255, verbose_name="عنوان القصيدة")
    body = models.TextField(
        verbose_name="نص القصيدة", help_text="أدخل نص القصيدة كاملاً هنا."
    )
    # --- ربط المستخدم ---
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # يربط بنموذج المستخدم النشط في Django
        related_name="poems",  # اسم للوصول إلى قصائد المستخدم من كائن المستخدم (user.poems.all())
        on_delete=models.CASCADE,  # إذا تم حذف المستخدم، احذف قصائده أيضًا
        verbose_name="الشاعر",  # اسم الحقل في الواجهات
    )
    # --- نهاية ربط المستخدم ---
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ آخر تحديث")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "قصيدة"
        verbose_name_plural = "قصائد"

    def __str__(self):
        return self.title
