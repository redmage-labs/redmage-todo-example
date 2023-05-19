from redmage import Component


class ComponentRegistryMixin:
    component_registry = {}

    def __init_subclass__(cls, **kwargs):
        alias = cls.alias if hasattr(cls, "alias") else cls.__name__
        cls.register_component(alias, cls)

        return super().__init_subclass__(**kwargs)

    @classmethod
    def register_component(cls, alias: str, component: Component):
        cls.component_registry[alias] = component

    @classmethod
    def get_component(cls, alias: str, *args, **kwargs):
        args = () if args == (None,) else args
        component = cls.component_registry.get(alias)
        if not component:
            raise RuntimeError(f"Unknown component alias: {alias}")
        return component(*args, **kwargs)
