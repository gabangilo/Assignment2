from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # recommended by django to fix import issues
    def ready(self):

        import users.signals
