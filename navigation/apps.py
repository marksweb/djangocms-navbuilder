"""
.. module:: navigation.apps
   :synopsis: App configuration for the navigation app
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NavigationConfig(AppConfig):
    """ App config for the navigation app """
    default_auto_field = "django.db.models.BigAutoField"
    name = 'navigation'
    verbose_name = _('Navigation')
