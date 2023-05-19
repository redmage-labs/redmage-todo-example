from typing import Optional

from jinja2 import Environment, FileSystemLoader, Template
from redmage import Component, elements

from .. import db
from .component_registry import ComponentRegistryMixin


class Jinja2Component(Component, ComponentRegistryMixin):
    template: Optional[str]
    template_path: Optional[str]

    def __init_subclass__(cls, routes=None, **kwargs):
        if hasattr(cls, "template_path"):
            env = Environment(loader=FileSystemLoader("."))
            cls.template_obj = env.get_template(cls.template_path)
        else:
            cls.template_obj = Template(cls.template)

        return super().__init_subclass__(routes=routes, **kwargs)

    def set_element_id(self, el):
        # Manually add the id in the template
        return el

    def render(self, **exts):
        output = self.template_obj.render(
            component=self,
            db=db,
            **{**exts, **elements.__dict__, **self.component_registry},
        )
        return output
