# backend/poems/admin.py

from django.contrib import admin
from .models import Poem  # استيراد نموذج القصيدة


@admin.register(Poem)
class PoemAdmin(admin.ModelAdmin):
    """
    تخصيص عرض وإدارة نموذج القصيدة في لوحة تحكم Django.
    """

    list_display = (
        "title",
        # 'owner', # سنضيفه لاحقاً بعد تفعيل ربط المستخدم
        "created_at",
        "updated_at",
    )
    search_fields = (
        "title",
        "body",
        # 'owner__username' # للبحث باسم المستخدم المالك (لاحقاً)
    )
    list_filter = (
        "created_at",
        "updated_at",
        # 'owner' # للفلترة حسب المالك (لاحقاً)
    )
    # يمكنك إضافة تخصيصات أخرى هنا، مثل حقول القراءة فقط إذا أردت
    # readonly_fields = ('created_at', 'updated_at')
