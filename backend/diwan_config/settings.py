# backend/diwan_config/settings.py

from pathlib import Path
import os

# ==> تأكدي من أن BASE_DIR معرف بشكل صحيح باستخدام pathlib <==
BASE_DIR = Path(__file__).resolve().parent.parent 

# !!! مهم: استخدمي المفتاح السري الأصلي إذا كان لديكِ !!!
SECRET_KEY = "django-insecure-YOUR_SECRET_KEY_HERE" # <-- استبدليه بالمفتاح الأصلي

DEBUG = True

# ==> هام لـ Gitpod: إضافة Host الخاص بـ Gitpod <==
# يمكنكِ استخدام '*' للتسهيل في بيئة التطوير، أو الحصول على الـ URL الديناميكي
ALLOWED_HOSTS = ['*'] # السماح بكل الـ Hosts (آمن في Gitpod غالباً)

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

# --- قسم قاعدة البيانات (معدل لـ Gitpod) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diwan_db_gitpod',  # <-- اسم قاعدة بيانات جديد لـ Gitpod
        'USER': 'gitpod',          # <-- مستخدم PostgreSQL الافتراضي في Gitpod
        'PASSWORD': '',             # <-- كلمة المرور (عادة فارغة للمستخدم gitpod)
        'HOST': 'localhost',       # <-- سيتم تشغيله داخل Gitpod بواسطة الخدمة
        'PORT': '5432',            # <-- المنفذ الافتراضي لـ PostgreSQL
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

# --- إعدادات Django REST Framework (كما هي) ---
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    ],
}
# --- نهاية إعدادات DRF ---

# ==> هام لـ Gitpod: إضافة إعدادات CORS إذا لزم الأمر <==
# إذا واجهتِ مشاكل CORS عند الاتصال من تطبيق Flutter، قد تحتاجين لإضافة:
# INSTALLED_APPS += ['corsheaders']
# MIDDLEWARE += ['corsheaders.middleware.CorsMiddleware']
# CORS_ALLOWED_ORIGINS = [
#    "https://YOUR_FLUTTER_APP_URL_FROM_GITPOD", # الـ URL الذي يعمل عليه تطبيق Flutter
# ]
# أو للتسهيل في التطوير (أقل أماناً):
# CORS_ALLOW_ALL_ORIGINS = True 