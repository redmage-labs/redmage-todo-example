from typing import Optional

from ..jinja2_component import Jinja2Component
from ..todo_router_component import TodoRouterComponent


class TodoAppComponent(
    Jinja2Component,
    routes=(
        "/",
        "/{route:Route}",
        "/{route:Route}/{todo_id:int}",
    ),
):
    template_path = "todos/components/todo_app_component/template.html"

    def __init__(self, route: str = "list", todo_id: "Optional[int]" = None):
        self.todo_id = todo_id
        self.route = route
        self.router_component = TodoRouterComponent
