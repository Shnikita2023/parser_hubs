from django.apps import AppConfig


class ArcticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
    verbose_name: str = 'Статьи'
