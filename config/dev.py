from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]  # dev only

# Optional: verbose email backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
