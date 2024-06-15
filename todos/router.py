from enum import Enum

from starlette.convertors import Convertor

from todos.components.todo_detail_component import TodoDetailComponent
from todos.components.todo_list_component import TodoListComponent


class RouteType(Enum):
    TODOS = ("todos", TodoListComponent)
    TODO_DETAIL = ("todo", TodoDetailComponent)

    def __init__(self, route, component):
        self.route = route
        self.component = component

    @staticmethod
    def to_dict():
        return {route.route: route.component for route in RouteType}

    @classmethod
    def get_component(cls, route: str, todo_id):
        component = RouteType.to_dict().get(route)
        if not component:
            raise RuntimeError(f"Unknown component route: {route}")
        if todo_id:
            return component(todo_id)
        else:
            return component()


class RouteConvertor(Convertor):
    regex = "|".join(RouteType.to_dict())

    def convert(self, value: str) -> str:
        return value

    def to_string(self, value: str) -> str:
        return value
