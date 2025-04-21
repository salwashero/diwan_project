# backend/poems/serializers.py

from rest_framework import serializers

# تأكد من استيراد نموذج المستخدم إذا لم تكن قد فعلت ذلك (نحتاجه ضمنيًا لـ owner.username)
# from django.contrib.auth import get_user_model
from .models import Poem

# User = get_user_model() # يمكنك استخدامه إذا احتجت للتعامل مع نموذج المستخدم مباشرة


class PoemSerializer(serializers.ModelSerializer):
    """
    Serializer لتحويل كائنات Poem إلى JSON والعكس.
    يتضمن معلومات المالك للقراءة فقط.
    """

    # إضافة حقل لعرض اسم المستخدم المالك للقراءة فقط
    # source='owner.username' يخبر السيريالايزر بجلب قيمة الحقل username من الكائن المرتبط في حقل owner
    owner_username = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Poem
        # تأكد من تضمين الحقول المطلوبة في القائمة
        fields = [
            "id",
            "title",
            "body",
            "owner",  # <<< يعرض ID المالك (يجب أن يكون هنا)
            "owner_username",  # <<< يعرض اسم مستخدم المالك (يجب أن يكون هنا)
            "created_at",
            "updated_at",
        ]
        # الحقول التي لا يمكن للمستخدم تعديلها مباشرة عبر بيانات الإدخال
        # المالك يتم تعيينه برمجيًا في perform_create
        read_only_fields = ["id", "owner", "owner_username", "created_at", "updated_at"]
