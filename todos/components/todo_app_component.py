from typing import Optional

import redmage.elements as el
from redmage import Component

from ..router import RouteType


class TodoAppComponent(
    Component,
    routes=("/", "/{route:Route}", "/{route:Route}/{todo_id:str}"),
):
    def __init__(
        self,
        route: str = RouteType.TODOS.route,
        todo_id: Optional[str] = None,
    ):
        self.route = route
        self.todo_id = todo_id

    async def render(self):
        return el.Doc(
            el.Html(
                el.Head(
                    el.Title("Todos"),
                    el.Meta(charset="utf-8"),
                    el.Meta(
                        name="viewport", content="width=device-width, initial-scale=1"
                    ),
                    el.Meta(
                        name="description",
                        content="Todos",
                    ),
                    el.Link(
                        rel="stylesheet",
                        href="https://unpkg.com/missing.css@1.1.2",
                    ),
                    el.Link(rel="stylesheet", href="/static/styles/core.css"),
                    el.Link(
                        rel="icon",
                        _type="image/x-icon",
                        href="/static/favicon.ico",
                    ),
                ),
                el.Body(
                    el.Main(
                        RouteType.get_component(self.route, self.todo_id),
                        _class="container",
                    ),
                    el.Script(
                        src="https://unpkg.com/htmx.org@1.9.12",
                        integrity="sha384-ujb1lZYygJmzgSwoxRggbCHcjc0rB2XoQrxeTUQyRjrOnlCoYta87iKBWq3EsdM2",  # noqa
                        crossorigin="anonymous",
                    ),
                ),
                lang="en",
            )
        )
