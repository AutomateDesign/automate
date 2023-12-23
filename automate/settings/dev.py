from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!



DEBUG = False


# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: define the correct hosts in production!

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



try:
    from .local import *
except ImportError:
    pass

