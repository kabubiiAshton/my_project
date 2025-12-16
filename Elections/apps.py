from django.apps import AppConfig
from django.db.utils import OperationalError

class ElectionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Elections'

    def ready(self):
        try:
            # Import models here, inside ready()
            from django.contrib.auth.models import Group
            Group.objects.get_or_create(name='Admin')
        except OperationalError:
            # Database isn't ready yet
            pass

# class ElectionsConfig(AppConfig):
#     name = 'Elections'
#
#     def ready(self):
#         # create groups if missing
#         from django.contrib.auth.models import Group, Permission
#         from django.contrib.contenttypes.models import ContentType
#         from django.contrib.auth import get_user_model
#
#         Group.objects.get_or_create(name='Admin')
#         Group.objects.get_or_create(name='ElectionManager')
#         Group.objects.get_or_create(name='Voter')
#
#     default_auto_field = 'django.db.models.BigAutoField'

