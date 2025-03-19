"""Конфигурация URL для проекта config.

Список `urlpatterns` направляет URL к представлениям.

Примеры:
Function views
    1. Добавить импорт:  from my_app import views
    2. Добавить URL в urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Добавить импорт:  from other_app.views import Home
    2. Добавить URL в urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Импортируйте функцию include(): from django.urls import include, path
    2. Добавить URL в urlpatterns:  path('blog/', include('blog.urls'))
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('django_polls.urls')),
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
