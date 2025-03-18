"""Конфигурация ASGI для проекта config.

Он отображает вызываемый ASGI как переменную уровня модуля с именем ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
