# backend/poems/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PoemViewSet

# إنشاء Router وتسجيل الـ ViewSet الخاص بنا معه.
router = DefaultRouter()
router.register(r"poems", PoemViewSet, basename="poem")
# r'poems' هو البادئة للـ URL (مثلاً /api/poems/)
# PoemViewSet هو الـ ViewSet الذي سيتعامل مع الطلبات لهذه البادئة
# basename='poem' يستخدم لتوليد أسماء الـ URL تلقائيًا

# يتم إنشاء روابط الـ API تلقائيًا بواسطة الـ Router.
# لا تحتاج لإضافة روابط list, create, retrieve, update, destroy يدويًا.
urlpatterns = [
    path("", include(router.urls)),  # تضمين الروابط التي أنشأها الـ Router
]
