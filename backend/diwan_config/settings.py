# backend/diwan_config/settings.py

from pathlib import Path
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# !!! مهم: إذا كان لديك مفتاح سري تم إنشاؤه تلقائيًا، استخدمه بدلاً من هذا !!!
SECRET_KEY = "django-insecure-YOUR_SECRET_KEY_HERE"  # استخدم المفتاح الأصلي إن وجد

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "poems.apps.PoemsConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "diwan_config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "diwan_config.wsgi.application"

# --- قسم قاعدة البيانات ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "diwan_db",  # اسم قاعدة البيانات (يجب أن يكون تم إنشاؤه)
        "USER": "diwan_user",  # اسم المستخدم (يجب أن يكون تم إنشاؤه)
        "PASSWORD": "omershary+@123",  # <<< === تم التغيير هنا ===
        "HOST": "localhost",  # عادةً يبقى كما هو
        "PORT": "5432",  # المنفذ الافتراضي
    }
}
# --- نهاية قسم قاعدة البيانات ---

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ar"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# backend/diwan_config/settings.py
# ... (كل الإعدادات الأخرى فوق هذا) ...

# --- إعدادات Django REST Framework ---
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # يسمح بالمصادقة عبر الجلسات (لواجهة DRF والمتصفح)
        "rest_framework.authentication.SessionAuthentication",
        # يسمح بالمصادقة عبر التوكن (لتطبيق الموبايل والـ APIs الخارجية)
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # الصلاحية الافتراضية (يمكن تجاوزها في الـ Views)
        # سنتركها IsAuthenticatedOrReadOnly مبدئيًا كافتراضي عام
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
    # يمكنك إضافة إعدادات أخرى لـ DRF هنا (مثل pagination, throttling)
}
# --- نهاية إعدادات DRF ---
