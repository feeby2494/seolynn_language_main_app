from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "seolynn_language_main_app.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import seolynn_language_main_app.users.signals  # noqa F401
        except ImportError:
            pass
