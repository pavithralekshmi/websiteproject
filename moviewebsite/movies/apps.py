from django.apps import AppConfig


class MovieappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'

    def ready(self):
        import movies.signals