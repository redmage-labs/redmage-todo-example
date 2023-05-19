from redmage import Target

from ... import db
from ..jinja2_component import Jinja2Component


class TodoAddComponent(Jinja2Component):
    template_path = "todos/components/todo_add_component/template.html"
    alias = "add"

    @Target.post
    def add_todo(self, todo: db.Todo, /):
        db.create_todo(todo.message, False)
        return self.get_component("list")
