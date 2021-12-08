from django.conf import settings
from django.db import models
from django.utils.translation import get_language, ugettext_lazy as _

from cms.models import CMSPlugin
from cms.models.fields import PageField
from djangocms_attributes_field.fields import AttributesField

TEMPLATE_DEFAULT = "default"


def get_templates():
    """ Get the available templates """
    choices = [(TEMPLATE_DEFAULT, _("Default"))]
    choices += getattr(settings, "DJANGOCMS_NAVIGATION_TEMPLATES", [])
    return choices


class NavigationContainerModel(CMSPlugin):
    """ Parent plugin containing navigation items """

    class Meta:
        """
        Metadata
        """
        app_label = 'navigation'
        verbose_name = 'Navigation container'
        verbose_name_plural = 'Navigation containers'

    name = models.CharField(
        blank=True,
        max_length=255,
        help_text=_("Optional name to help identify this plugin")
    )
    list_attributes = AttributesField()
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )

    def __str__(self):
        """ String representation of the model """
        if self.name:
            return self.name
        else:
            return self.id


class NavigationItemModel(CMSPlugin):
    """ Navigation item plugin, defining links in the navigation container """

    class Meta:
        """
        Metadata
        """
        app_label = 'navigation'
        verbose_name = 'Navigation item'
        verbose_name_plural = 'Navigation items'

    link_internal = PageField(
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    link_external = models.URLField(
        blank=True
    )
    link_label = models.CharField(
        blank=True,
        max_length=1024
    )
    list_item_attributes = AttributesField()
    link_attributes = AttributesField()
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )

    def __str__(self):
        """ String representation of this navigation item """
        if self.link_internal:
            language = get_language()
            if language:
                return '(' + str(self.link_internal.title_set.get(language=language).title) + ')'
            else:
                return '(' + str(self.link_internal.title_set.first().title) + ')'
        else:
            return '(' + self.link_external + ')'

    def get_url(self):
        """ Get the URL for this navigation item """
        if self.link_internal:
            return self.link_internal.get_absolute_url()
        else:
            return self.link_external

    def get_label(self):
        """ Get the appropriate label for the navigation item """
        if self.link_label:
            return self.link_label
        elif self.link_internal:
            language = get_language()
            if language:
                return self.link_internal.title_set.get(language=language).title
            else:
                return self.link_internal.title_set.first().title
        else:
            return self.link_external
