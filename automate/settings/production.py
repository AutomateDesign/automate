from .base import *



DEBUG = False

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"




try:
    from .local import *
except ImportError:
    pass




