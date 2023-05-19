from typing import Optional

from redmage import Component, Target

from .. import Jinja2Component


class TodoRouterComponent(Jinja2Component):
    template_path = "todos/components/todo_router_component/template.html"

    def __init__(self, route: str = "list", todo_id: "Optional[int]" = None):
        self.todo_id = todo_id
        self.route = route
        Component.add_render_extension(router=self.router)

    @Target.get
    def router(self, route: str, todo_id: "Optional[int]" = None):
        self.route = route
        self.todo_id = todo_id
        return self
