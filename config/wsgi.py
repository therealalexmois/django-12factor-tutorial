"""Конфигурация WSGI для проекта config.

Он отображает вызываемый модуль WSGI как переменную уровня модуля с именем ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
