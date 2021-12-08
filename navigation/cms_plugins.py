from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import NavigationContainerModel, NavigationItemModel


@plugin_pool.register_plugin
class NavigationPlugin(CMSPluginBase):
    allow_children = True
    model = NavigationContainerModel
    module = 'Navigation'
    name = 'Navigation'
    child_classes = [
        'NavigationItemPlugin'
    ]

    def get_render_template(self, context, instance, placeholder):
        """
        Return the template to render
        """
        return f'navigation/{instance.template}/navigation_plugin.html'


@plugin_pool.register_plugin
class NavigationItemPlugin(CMSPluginBase):
    model = NavigationItemModel
    module = 'Navigation'
    name = 'Navigation item'
    allow_children = True
    parent_classes = [
        'NavigationPlugin'
    ]
    child_classes = [
        'NavigationItemChildPlugin'
    ]

    def get_render_template(self, context, instance, placeholder):
        """
        Return the template to render
        """
        return f'navigation/{instance.template}/navigation_plugin_item.html'


@plugin_pool.register_plugin
class NavigationItemChildPlugin(CMSPluginBase):
    module = 'Navigation'
    model = NavigationItemModel
    name = 'Navigation item child'
    allow_children = False
    parent_classes = [
        'NavigationItemPlugin'
    ]

    def get_render_template(self, context, instance, placeholder):
        """
        Return the template to render
        """
        return f'navigation/{instance.template}/navigation_plugin_item_child.html'
