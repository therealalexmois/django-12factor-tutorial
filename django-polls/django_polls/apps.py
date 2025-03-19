"""Модуль конфигурации приложения."""

from django.apps import AppConfig


class PollsConfig(AppConfig):
    """Класс конфигурации приложения.

    Класс определяет настройки на уровне приложения, такие как тип поля по умолчанию
    автогенерируемый тип поля для моделей.
    """

    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'django_polls'
    label: str = 'polls'
