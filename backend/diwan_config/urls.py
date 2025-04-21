# backend/diwan_config/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import (
    obtain_auth_token,
)  # <<< استيراد view الحصول على التوكن

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("poems.urls")),  # روابط API القصائد
    # --- إضافة رابط للحصول على التوكن ---
    # عند إرسال POST request يحتوي على username و password إلى هذا الرابط،
    # سيُرجع التوكن الخاص بالمستخدم إذا كانت بيانات الاعتماد صحيحة.
    path("api/token-auth/", obtain_auth_token, name="api_token_auth"),
    # --- نهاية رابط التوكن ---
]
