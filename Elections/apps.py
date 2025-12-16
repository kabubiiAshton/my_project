from django.apps import AppConfig

class ElectionsConfig(AppConfig):
    name = 'Elections'

    def ready(self):
        # create groups if missing
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        from django.contrib.auth import get_user_model

        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='ElectionManager')
        Group.objects.get_or_create(name='Voter')

    default_auto_field = 'django.db.models.BigAutoField'

