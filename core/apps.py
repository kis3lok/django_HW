from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = 'Барбершоп "Hard Rock"'
    
    def ready(self):
        import core.signals
